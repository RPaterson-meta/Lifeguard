from app import app
from flask import redirect, request, flash
from app.views.viewfunctions import point_perimeta, lifeguard_render, store_kit_bookings, get_kit_bookings, update_deployment_availability
from app.forms import ClearwaterKitBookingForm, PerimetaKitBookingForm, VolteKitBookingForm, CCFKitBookingForm
import datetime
import os


@app.route('/clearwater_kit_booking', methods=['POST'])
def clearwater_kit_booking():
    clearwater_form = ClearwaterKitBookingForm()
    if request.method == 'POST' and clearwater_form.name.data:
        book_clearwater_kit(clearwater_form)
        flash('Clearwater kit booked for ' + str(clearwater_form.name.data), 'success')
    elif request.method == 'POST':
        flash('Please enter initials', 'error')
    return redirect('/kit_management')


@app.route('/volte_kit_booking', methods=['POST'])
def volte_kit_booking():
    volte_form = VolteKitBookingForm()
    if request.method == 'POST' and volte_form.name.data:
        book_volte_kit(volte_form)
        flash('VoLTE kit booked for ' + str(volte_form.name.data), 'success')
    elif request.method == 'POST':
        flash('Please enter initials', 'error')
    return redirect('/kit_management')


@app.route('/perimeta_kit_booking', methods=['POST'])
def perimeta_kit_booking():
    perimeta_form = PerimetaKitBookingForm()
    print(perimeta_form.pointing.data)
    if request.method == 'POST':
        if not perimeta_form.name.data:
            flash('Please enter initials', 'error')
        elif perimeta_form.pointing.data == 'Select Deployment':
            flash('Please enter the deployment you will be pointing Perimeta at', 'error')
        else:
            if perimeta_form.use_pointing.data:
                point_perimeta(perimeta_form.pointing.data)
            book_perimeta_kit(perimeta_form)
            flash('Perimeta booked for ' + str(perimeta_form.name.data), 'success')
    return redirect('/kit_management')


@app.route('/ccf_kit_booking', methods=['POST'])
def ccf_kit_booking():
    ccf_form = CCFKitBookingForm()
    if request.method == 'POST' and ccf_form.name.data:
        book_ccf_kit(ccf_form)
        flash('CCF kit booked for ' + str(ccf_form.name.data), 'success')
    elif request.method == 'POST':
        flash('Please enter initials', 'error')
    return redirect('/kit_management')


@app.route('/clearwater_kit_release', methods=['POST'])
def clearwater_kit_release():
    clearwater_form = ClearwaterKitBookingForm()
    if request.method == 'POST' and clearwater_form.name.data:
        release_clearwater_kit(clearwater_form)
        flash('Kit released for ' + str(clearwater_form.name.data), 'success')
    elif request.method == 'POST':
        flash('Please enter initials', 'error')
    return redirect('/kit_management')


@app.route('/volte_kit_release', methods=['POST'])
def volte_kit_release():
    volte_form = VolteKitBookingForm()
    if request.method == 'POST' and volte_form.name.data:
        release_volte_kit(volte_form)
        flash('VoLTE kit released for ' + str(volte_form.name.data), 'success')
    elif request.method == 'POST':
        flash('Please enter initials', 'error')
    return redirect('/kit_management')


@app.route('/ccf_kit_release', methods=['POST'])
def ccf_kit_release():
    ccf_form = CCFKitBookingForm()
    if request.method == 'POST' and ccf_form.name.data:
        release_ccf_kit(ccf_form)
        flash('CCF kit released for ' + str(ccf_form.name.data), 'success')
    elif request.method == 'POST':
        flash('Please enter initials', 'error')
    return redirect('/kit_management')


@app.route('/perimeta_kit_release', methods=['POST'])
def perimeta_kit_release():
    perimeta_form = PerimetaKitBookingForm()
    if request.method == 'POST':
        if not perimeta_form.name.data:
            flash('Please enter initials', 'error')
        elif not perimeta_form.pointing.data:
            flash('Please enter the deployment Perimeta is pointing at', 'error')
        else:
            if perimeta_form.use_pointing.data:
                point_perimeta(perimeta_form.pointing.data)
            release_perimeta_kit(perimeta_form)
            flash('Perimeta released for ' + str(perimeta_form.name.data), 'success')
    return redirect('/kit_management')

##########################################
##########################################
##########################################
##########################################
##########################################
##########################################
# required functions


def book_clearwater_kit(form):
    log_clearwater_kit_booking(form)
    bookings = get_kit_bookings()
    # clearwater specific
    for deployment in form.deployments:

        for node in deployment['nodes']:
            if node.data:
                bookings['clearwater'][deployment['name']]['nodes'][
                    node.name]['available'] = False
                bookings['clearwater'][deployment['name']]['nodes'][
                    node.name]['tooltip'] = generate_tooltip(form)

            update_deployment_availability('clearwater', deployment, bookings)
    store_kit_bookings(bookings)


def book_volte_kit(form):
    log_volte_kit_booking(form)
    bookings = get_kit_bookings()
    # clearwater specific
    for deployment in form.deployments:

        for node in deployment['nodes']:
            if node.data:
                bookings['volte'][deployment['name']]['nodes'][
                    node.name]['available'] = False
                bookings['volte'][deployment['name']]['nodes'][
                    node.name]['tooltip'] = generate_tooltip(form)

            update_deployment_availability('volte', deployment, bookings)
    store_kit_bookings(bookings)


def book_ccf_kit(form):
    log_ccf_kit_booking(form)
    bookings = get_kit_bookings()
    # clearwater specific
    for deployment in form.deployments:

        for node in deployment['nodes']:
            if node.data:
                bookings['ccf'][deployment['name']]['nodes'][
                    node.name]['available'] = False
                bookings['ccf'][deployment['name']]['nodes'][
                    node.name]['tooltip'] = generate_tooltip(form)

            update_deployment_availability('ccf', deployment, bookings)
    store_kit_bookings(bookings)


def log_clearwater_kit_booking(form):

    with open(os.path.dirname(__file__) + '/../../logs/clearwater_kit-' + datetime.datetime.today().strftime('%b_%Y') + '.log', 'a') as bookings_ledger:
        bookings_ledger.write('\nBOOKING: ' + datetime.datetime.today().strftime("%d/%m/%Y  %H:%M:%S"))
        bookings_ledger.write('\nuser_of_the_nodes: ' + form.name.data)
        for deployment in form.deployments:
            for node in deployment['nodes']:
                if node.data:
                    bookings_ledger.write('\n' + node.name)
                    bookings_ledger.write(' - type=BOOKING')
                    bookings_ledger.write(' - user=' + form.name.data)
                    bookings_ledger.write(' - note=' + form.note.data)
        bookings_ledger.write(
            '\nfurther_nodes_use_information: ' + str(form.note.data))
        bookings_ledger.write('\n')


def log_volte_kit_booking(form):

    with open(os.path.dirname(__file__) + '/../../logs/volte_kit-' + datetime.datetime.today().strftime('%b_%Y') + '.log', 'a') as bookings_ledger:
        bookings_ledger.write('\nBOOKING: ' + datetime.datetime.today().strftime("%d/%m/%Y  %H:%M:%S"))
        bookings_ledger.write('\nuser_of_the_nodes: ' + form.name.data)
        for deployment in form.deployments:
            for node in deployment['nodes']:
                if node.data:
                    bookings_ledger.write('\n' + node.name)
                    bookings_ledger.write(' - type=BOOKING')
                    bookings_ledger.write(' - user=' + form.name.data)
                    bookings_ledger.write(' - note=' + form.note.data)
        bookings_ledger.write(
            '\nfurther_nodes_use_information: ' + str(form.note.data))
        bookings_ledger.write('\n')


def log_ccf_kit_booking(form):

    with open(os.path.dirname(__file__) + '/../../logs/ccf_kit-' + datetime.datetime.today().strftime('%b_%Y') + '.log', 'a') as bookings_ledger:
        bookings_ledger.write('\nBOOKING: ' + datetime.datetime.today().strftime("%d/%m/%Y  %H:%M:%S"))
        bookings_ledger.write('\nuser_of_the_nodes: ' + form.name.data)
        for deployment in form.deployments:
            for node in deployment['nodes']:
                if node.data:
                    bookings_ledger.write('\n' + node.name)
                    bookings_ledger.write(' - type=BOOKING')
                    bookings_ledger.write(' - user=' + form.name.data)
                    bookings_ledger.write(' - note=' + form.note.data)
        bookings_ledger.write(
            '\nfurther_nodes_use_information: ' + str(form.note.data))
        bookings_ledger.write('\n')


def generate_tooltip(form):
    name = form.name.data
    note = form.note.data
    other_nodes = [node.name for node in form.form_nodes if node.data]
    rtn_string = '<p style="font-weight: bold;">Booked by: </p><p>' + name.upper() + '</p>'
    rtn_string += '<p style="font-weight: bold;">Nodes booked:' + '</p>'
    for node in other_nodes:
        rtn_string += '<p>' + node + '</p>'
    rtn_string += '<p style="font-weight: bold;">Note: </p><p>' + note + '</p'
    return rtn_string


def generate_perimeta_book_tooltip(form):
    name = form.name.data
    note = form.note.data
    pointing = form.pointing.data
    rtn_string = '<p style="font-weight: bold;">Booked by: </p><p>' + name.upper() + '</p>'
    rtn_string += '<p style="font-weight: bold;">Pointing at:</p><p>' + pointing + '</p>'
    rtn_string += '<p style="font-weight: bold;">Note: </p><p>' + note + '</p>'
    return rtn_string


def generate_perimeta_release_tooltip(form):
    name = form.name.data
    note = form.note.data
    pointing = form.pointing.data
    rtn_string = '<p style="font-weight: bold;">Released by: </p><p>' + name.upper() + '</p>'
    rtn_string += '<p style="font-weight: bold;">Pointing at: </p><p>' + pointing + '</p>'
    rtn_string += '<p style="font-weight: bold;">Note: </p><p>' + note + '</p>'
    rtn_string += '<p style="font-weight: bold;">PERIMETA IS FREE </p>'
    return rtn_string


def log_perimeta_kit_booking(form):
    with open(os.path.dirname(__file__) + '/../../logs/perimeta_kit-' + datetime.datetime.today().strftime('%b_%Y') + '.log', 'a') as bookings_ledger:
        bookings_ledger.write('\nBOOKING: ' + datetime.datetime.today().strftime("%d/%m/%Y  %H:%M:%S"))
        bookings_ledger.write('\nreleaser_of_perimeta: ' + form.name.data)
        bookings_ledger.write('\nPerimeta now pointing at: ' + form.pointing.data)
        bookings_ledger.write('\nL3_cc_perim1')
        bookings_ledger.write(' - type=BOOKING')
        bookings_ledger.write(' - user=' + form.name.data)
        bookings_ledger.write(' - pointing_at=' + form.pointing.data)
        bookings_ledger.write(' - note=' + form.note.data)
        bookings_ledger.write(
            '\nfurther_nodes_booking_information: ' + str(form.note.data))
        bookings_ledger.write('\n')


def book_perimeta_kit(form):
    log_perimeta_kit_booking(form)
    bookings = get_kit_bookings()
    # clearwater specific
    bookings['perimeta']['available'] = False
    bookings['perimeta']['pointing_at'] = form.pointing.data
    bookings['perimeta']['tooltip'] = generate_perimeta_book_tooltip(form)
    store_kit_bookings(bookings)


def log_kit_release(form, product='clearwater'):
    with open(os.path.dirname(__file__) + '/../../logs/' + product + '_kit-' + datetime.datetime.today().strftime('%b_%Y') + '.log', 'a') as bookings_ledger:
        bookings_ledger.write('\nRELEASE: ' + datetime.datetime.today().strftime("%d/%m/%Y  %H:%M:%S"))
        bookings_ledger.write('\nreleaser_of_the_nodes: ' + form.name.data)
        for deployment in form.deployments:
            for node in deployment['nodes']:
                if node.data:
                    bookings_ledger.write('\n' + node.name)
                    bookings_ledger.write(' - type=RELEASE')
                    bookings_ledger.write(' - user=' + form.name.data)
                    bookings_ledger.write(' - note=' + form.note.data)
        bookings_ledger.write(
            '\nfurther_nodes_release_information: ' + str(form.note.data))
        bookings_ledger.write('\n')


def release_clearwater_kit(form):
    log_kit_release(form)
    bookings = get_kit_bookings()
    for deployment in form.deployments:
        for node in deployment['nodes']:
            if node.data:
                bookings['clearwater'][deployment['name']]['nodes'][node.name]['available'] = True
        update_deployment_availability('clearwater', deployment, bookings)
    store_kit_bookings(bookings)


def release_volte_kit(form):
    log_kit_release(form, product='volte')
    bookings = get_kit_bookings()
    for deployment in form.deployments:
        for node in deployment['nodes']:
            if node.data:
                bookings['volte'][deployment['name']]['nodes'][node.name]['available'] = True
        update_deployment_availability('volte', deployment, bookings)
    store_kit_bookings(bookings)


def release_ccf_kit(form):
    log_kit_release(form, product='ccf')
    bookings = get_kit_bookings()
    for deployment in form.deployments:
        for node in deployment['nodes']:
            if node.data:
                bookings['ccf'][deployment['name']]['nodes'][node.name]['available'] = True
        update_deployment_availability('ccf', deployment, bookings)
    store_kit_bookings(bookings)


def release_perimeta_kit(form):
    log_perimeta_kit_release(form)
    bookings = get_kit_bookings()
    bookings['perimeta']['available'] = True
    bookings['perimeta']['pointing_at'] = form.pointing.data
    bookings['perimeta']['tooltip'] = generate_perimeta_release_tooltip(form)
    store_kit_bookings(bookings)


def log_perimeta_kit_release(form):
    with open(os.path.dirname(__file__) + '/../../logs/perimeta_kit-' + datetime.datetime.today().strftime('%b_%Y') + '.log', 'a') as bookings_ledger:
        bookings_ledger.write('\nRELEASE: ' + datetime.datetime.today().strftime("%d/%m/%Y  %H:%M:%S"))
        bookings_ledger.write('\nreleaser_of_perimeta: ' + form.name.data)
        bookings_ledger.write('\nPerimeta now pointing at: ' + form.pointing.data)
        bookings_ledger.write('\nL3_cc_perim1')
        bookings_ledger.write(' - type=RELEASE')
        bookings_ledger.write(' - user=' + form.name.data)
        bookings_ledger.write(' - pointing_at=' + form.pointing.data)
        bookings_ledger.write(' - note=' + form.note.data)
        bookings_ledger.write(
            '\nfurther_nodes_release_information: ' + str(form.note.data))
        bookings_ledger.write('\n')
