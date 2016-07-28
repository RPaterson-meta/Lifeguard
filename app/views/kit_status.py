from app import app
from flask import request, flash, redirect
from app.views.viewfunctions import lifeguard_render, read_dictionary_from_file, write_dictionary_to_file
from app.forms import KitBookingForm


@app.route('/kit_status', methods=['GET', 'POST'])
def kit_status():
    form = KitBookingForm()
    if request.method == 'POST' and form.name.data:
        release_kit(form)
        flash('Kit released by ' + str(form.name.data), 'success')
        return redirect('/index')
    elif request.method == 'POST':
        flash('Please enter initials', 'error')

    cc_deployments = read_dictionary_from_file(
        '/home/clearwater/rjp/l3dash/clearwater_kit_state.txt')
    cc_deployment_names = sorted(cc_deployments.keys())

    perimeta = {'name': 'L3 Perimeta', 'state': 'success'}
    return lifeguard_render("kit_status.html",
                            title='Kit Status',
                            form=form,
                            cc_deployments=cc_deployments,
                            cc_deployment_names=cc_deployment_names,
                            perimeta=perimeta)


def log_kit_release(form):
    with open('/home/clearwater/rjp/l3dash/clearwater_kit.log', 'a') as bookings_ledger:
        bookings_ledger.write('\nRELEASE')
        bookings_ledger.write('\nreleaser_of_the_nodes: ' + form.name.data)
        for deployment in form.clearwater_deployments:
            for node in deployment['nodes']:
                if node.data:
                    bookings_ledger.write('\n' + node.name)
                    bookings_ledger.write(' - user=' + form.name.data)
                    bookings_ledger.write(' - note=' + form.note.data)
        bookings_ledger.write(
            '\nfurther_nodes_release_information: ' + str(form.note.data))
        bookings_ledger.write('\n')


def release_kit(form):
    log_kit_release(form)
    bookings = read_dictionary_from_file(
        '/home/clearwater/rjp/l3dash/clearwater_kit_state.txt')
    for deployment in form.clearwater_deployments:
        for node in deployment['nodes']:
            if node.data:
                bookings[deployment['name']]['nodes'][node.name]['available'] = True
    write_dictionary_to_file(
        bookings, '/home/clearwater/rjp/l3dash/clearwater_kit_state.txt')
