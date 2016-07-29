from app import app
from flask import redirect, request, flash
from app.views.viewfunctions import lifeguard_render, store_kit_bookings, get_kit_bookings, update_deployment_availability
from app.forms import KitBookingForm


@app.route('/kit_booking', methods=['GET', 'POST'])
def kit_booking():
    form = KitBookingForm()
    if request.method == 'POST' and form.name.data:
        book_kit(form)
        flash('Kit booked for ' + str(form.name.data), 'success')
        return redirect('/index')
    elif request.method == 'POST':
        flash('Please enter initials', 'error')

    bookings = get_kit_bookings()

    return lifeguard_render('kit_booking.html',
                            title='Kit Booking',
                            form=form,
                            bookings=bookings)


def book_kit(form):
    log_kit_booking(form)
    bookings = get_kit_bookings()
    for deployment in form.clearwater_deployments:

        for node in deployment['nodes']:
            if node.data:
                bookings[deployment['name']]['nodes'][
                    node.name]['available'] = False
        update_deployment_availability(deployment, bookings)
    store_kit_bookings(bookings)


def log_kit_booking(form):
    with open('/home/clearwater/rjp/l3dash/clearwater_kit.log', 'a') as bookings_ledger:
        bookings_ledger.write('\nBOOKING')
        bookings_ledger.write('\nuser_of_the_nodes: ' + form.name.data)
        for deployment in form.clearwater_deployments:
            for node in deployment['nodes']:
                if node.data:
                    bookings_ledger.write('\n' + node.name)
                    bookings_ledger.write(' - type=BOOKING')
                    bookings_ledger.write(' - user=' + form.name.data)
                    bookings_ledger.write(' - note=' + form.note.data)
        bookings_ledger.write(
            '\nfurther_nodes_use_information: ' + str(form.note.data))
        bookings_ledger.write('\n')
