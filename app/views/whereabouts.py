import datetime
import pypyodbc as pyodbc
from app import app
from app.views.viewfunctions import lifeguard_render

TPR = {'initials': 'TPR', 'name': 'Tom Rees', 'payroll_id': 5349}
SL = {'initials': 'SL', 'name': 'Steve Lloyd', 'payroll_id': 164}
NJ2 = {'initials': 'NJ2', 'name': 'Nicole Johnson', 'payroll_id': 511}
RJP = {'initials': 'RJP', 'name': 'Ross Paterson', 'payroll_id': 1386}
NB = {'initials': 'NB', 'name': 'Neil Bruce', 'payroll_id': 361}

TEAM = [TPR, SL, NJ2, RJP, NB]


@app.route('/whereabouts')
def whereabouts():
    dates = []
    table_date_headings = []
    table_data = []
    today = datetime.datetime.today()
    monday = today - datetime.timedelta(int(today.strftime('%w')))

    for i in range(35):
        day = monday + datetime.timedelta(i)
        if day.strftime('%a') != 'Sat' and day.strftime('%a') != 'Sun':
            dates.append(day)

    date_from = str(dates[0].strftime('%Y-%m-%d'))
    date_to = dates[-1] + datetime.timedelta(1)
    date_to = str(date_to.strftime('%Y-%m-%d'))

    for date in dates:
        table_date_headings.append(date.strftime('%a %d %b'))

    for person in TEAM:
        row = []
        row.append({'text': person['initials'], 'style': None})
        row.append({'text': person['name'], 'style': None})
        row += get_whereabouts(person['payroll_id'], date_from, date_to)
        table_data.append(row)

    return lifeguard_render("whereabouts.html",
                            title='Whereabouts',
                            table_date_headings=table_date_headings,
                            table_data=table_data)


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
        entry = {'text': db_output[i][10][:3], 'style': 'state' + db_output[i][10].upper()}

        if db_output[i + 1][10] != db_output[i][10]:
            entry['text'] += '/' + db_output[i + 1][10][:3]
            entry['style'] = 'state' + db_output[i + 1][10].upper()

        wbts.append(entry)
    return wbts
