from app import app
from flask import request, flash
from app.views.viewfunctions import lifeguard_render, get_kit_bookings, store_kit_bookings, update_deployment_availability
from app.forms import ClearwaterKitBookingForm
import datetime
import os


@app.route('/kit_management', methods=['GET', 'POST'])
def kit_status():
    form = ClearwaterKitBookingForm()
    if request.method == 'POST' and form.name.data:
        release_kit(form)
        flash('Kit released by ' + str(form.name.data), 'success')
    elif request.method == 'POST':
        flash('Please enter initials', 'error')

    bookings = get_kit_bookings()
    cc_deployment_names = sorted(bookings['clearwater'].keys())

    return lifeguard_render("kit_management.html",
                            title='Kit Management',
                            form=form,
                            bookings=bookings,
                            cc_deployment_names=cc_deployment_names)


def log_kit_release(form):
    with open(os.path.dirname(__file__) + '/../../logs/clearwater_kit-' + datetime.datetime.today().strftime('%b_%Y') + '.log', 'a') as bookings_ledger:
        bookings_ledger.write('\nRELEASE')
        bookings_ledger.write('\nreleaser_of_the_nodes: ' + form.name.data)
        for deployment in form.clearwater_deployments:
            for node in deployment['nodes']:
                if node.data:
                    bookings_ledger.write('\n' + node.name)
                    bookings_ledger.write(' - type=RELEASE')
                    bookings_ledger.write(' - user=' + form.name.data)
                    bookings_ledger.write(' - note=' + form.note.data)
        bookings_ledger.write(
            '\nfurther_nodes_release_information: ' + str(form.note.data))
        bookings_ledger.write('\n')


def release_kit(form):
    log_kit_release(form)
    bookings = get_kit_bookings()
    for deployment in form.clearwater_deployments:
        for node in deployment['nodes']:
            if node.data:
                bookings['clearwater'][deployment['name']]['nodes'][node.name]['available'] = True
        update_deployment_availability('clearwater', deployment, bookings)
    store_kit_bookings(bookings)
