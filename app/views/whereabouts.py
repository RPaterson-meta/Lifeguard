import datetime
import pypyodbc as pyodbc
from app import app
from app.views.viewfunctions import lifeguard_render
# TO ADD OR REMOVE TEAM MEMBERS, SIMPLY GIVE THEM A DATASTRUCTURE LIKE THE MEMBERS
# BELOW AND THEN ADD THEM TO THE TEAM LIST BENEATH
TPR = {'initials': 'TPR', 'name': 'Thomas Rees', 'payroll_id': 5349}
SL = {'initials': 'SL', 'name': 'Steve Lloyd', 'payroll_id': 164}
NJ2 = {'initials': 'NJ2', 'name': 'Nicole Johnson', 'payroll_id': 511}
RJP = {'initials': 'RJP', 'name': 'Ross Paterson', 'payroll_id': 1386}
NB = {'initials': 'NB', 'name': 'Neil Bruce', 'payroll_id': 361}
TB = {'initials': 'TB', 'name': 'Tony Blenkinsopp', 'payroll_id': 165}
GF2 = {'initials': 'GF2', 'name': 'Grant Fitzgerald', 'payroll_id': 5097}
JWK = {'initials': 'JWK', 'name': 'James Kistruck', 'payroll_id': 441}


TEAM = [NJ2, SL, TPR, NB, GF2, JWK, TB]


@app.route('/whereabouts')
def whereabouts():
    dates = []

    today = datetime.datetime.today()
    monday = today - datetime.timedelta(int(today.strftime('%w')))

    for i in range(35):
        day = monday + datetime.timedelta(i)
        if day.strftime('%a') != 'Sat' and day.strftime('%a') != 'Sun':
            dates.append(day)

    date_from = str(dates[0].strftime('%Y-%m-%d'))
    # database doesn't return final date
    date_to = dates[-1] + datetime.timedelta(1)
    date_to = str(date_to.strftime('%Y-%m-%d'))

    table_date_headings = get_date_headings(today, dates)

    table_data = generate_table_data(date_from, date_to)

    return lifeguard_render("whereabouts.html",
                            title='Whereabouts',
                            table_date_headings=table_date_headings,
                            table_data=table_data,
                            image='/static/images/whereabouts.png')


def get_whereabouts(payroll_id, date_from, date_to):
    cnxn = pyodbc.connect(
        'DRIVER={FreeTDS};SERVER=KNOX;PORT=1433;DATABASE=employee;UID=public_directory_ro;PWD=Pdro6232HFfsdk;UseNTLMv2=yes;TDS_Version=8.0;Trusted_Domain=dcl;autocommit=True')
    cursor = cnxn.cursor()
    params = (payroll_id, date_from, date_to)
    sql = 'exec employee.public_ro.where_qry_emp @payroll=?, @start_date=?, @end_date=?'
    result = cursor.execute(sql, params)
    wbts = []
    db_output = result.fetchall()
    for i in range(0, len(db_output), 2):
        entry = {}
        morn = {'text': db_output[i][10][:3],
                'style': 'state' + db_output[i][10].upper()}
        aft = {'text': db_output[i + 1][10][:3],
               'style': 'state' + db_output[i + 1][10].upper()}

        if db_output[i][5].strftime('%a') == 'Fri':
            entry['style'] = 'endOfWeek'

        if morn['text'] != aft['text']:
            entry['split'] = True
            entry['morning'] = morn
            entry['afternoon'] = aft
        else:
            entry['split'] = False
            entry['day'] = aft
        wbts.append(entry)
    return wbts


def get_date_headings(today, dates):
    table_date_headings = []
    for date in dates:
        entry = {}
        entry['text'] = date.strftime('%a %d %b')
        entry['style'] = 'TH'
        if date == today:
            entry['style'] += ' today'
        if 'Fri' in entry['text']:
            entry['style'] += ' endOfWeek'
        table_date_headings.append(entry)
    return table_date_headings


def generate_table_data(date_from, date_to):
    table_data = []
    for person in TEAM:
        row = []
        initials_entry = {'text': person[
            'initials'], 'style': None}
        name_entry = {'text': person['name'], 'style': None}
        timezone_entry = {'text': 'Greenwich Mean Time (UTC)', 'style': None}
        row.append({'day': initials_entry, 'split': False})
        row.append({'day': name_entry, 'split': False})
        row.append({'day': timezone_entry, 'split': False})
        row += get_whereabouts(person['payroll_id'], date_from, date_to)
        table_data.append(row)
    return table_data
