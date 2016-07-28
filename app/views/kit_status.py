from app import app
from app.views.viewfunctions import lifeguard_render, read_dictionary_from_file, write_dictionary_to_file


@app.route('/kit_status')
def kit_status():
    l3_cc = {'name': 'L3 CC', 'state': 'success'}
    l3_cc2 = {'name': 'L3 CC2', 'state': 'danger'}
    l3_cc3 = {'name': 'L3 CC3', 'state': 'warning'}
    l3_cc4 = {'name': 'L3 CC4', 'state': 'success'}
    perimeta = {'name': 'L3 Perimeta', 'state': 'success'}
    cc_deployments = [l3_cc, l3_cc2, l3_cc3, l3_cc4]
    return lifeguard_render("kit_status.html",
                            title='Kit Status',
                            cc_deployments=cc_deployments,
                            perimeta=perimeta)


def log_kit_release(form):
    with open('/home/clearwater/rjp/l3dash/clearwater_kit.log', 'w') as bookings_ledger:
        bookings_ledger.write('\nBOOKING')
        bookings_ledger.write('\nuser_of_the_nodes: ' + form.name.data)
        for deployment in form.clearwater_deployments:
            for node in deployment['nodes']:
                if node.data:
                    bookings_ledger.write('\n' + node.name)
        bookings_ledger.write(
            '\nfurther_nodes_use_information: ' + str(form.note.data))
        bookings_ledger.write('\n')
