from app import app
from flask import redirect, request, flash
from app.views.viewfunctions import lifeguard_render, write_dictionary_to_file, read_dictionary_from_file
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

    bookings = read_dictionary_from_file(
        '/home/clearwater/rjp/l3dash/clearwater_kit_state.txt')

    return lifeguard_render('kit_booking.html',
                            title='Kit Booking',
                            form=form,
                            bookings=bookings)


def book_kit(form):
    log_kit_booking(form)
    bookings = read_dictionary_from_file(
        '/home/clearwater/rjp/l3dash/clearwater_kit_state.txt')
    for deployment in form.clearwater_deployments:
        for node in deployment['nodes']:
            if node.data:
                bookings[deployment['name']]['nodes'][node.name]['available'] = False
    write_dictionary_to_file(
        bookings, '/home/clearwater/rjp/l3dash/clearwater_kit_state.txt')


def log_kit_booking(form):
    with open('/home/clearwater/rjp/l3dash/clearwater_kit.log', 'a') as bookings_ledger:
        bookings_ledger.write('\nBOOKING')
        bookings_ledger.write('\nuser_of_the_nodes: ' + form.name.data)
        for deployment in form.clearwater_deployments:
            for node in deployment['nodes']:
                if node.data:
                    bookings_ledger.write('\n' + node.name)
                    bookings_ledger.write(' - user=' + form.name.data)
                    bookings_ledger.write(' - note=' + form.note.data)
        bookings_ledger.write(
            '\nfurther_nodes_use_information: ' + str(form.note.data))
        bookings_ledger.write('\n')
