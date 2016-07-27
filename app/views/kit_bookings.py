from app import app
from flask import redirect, request, flash
from app.views.viewfunctions import lifeguard_render
from app.forms import KitBookingForm


@app.route('/kit_bookings', methods=['GET', 'POST'])
def kit_bookings():
    form = KitBookingForm()
    if request.method == 'POST' and form.name.data:
        book_kit(form)
        flash('Kit booked for ' + str(form.name.data), 'success')
        return redirect('/index')
    elif request.method == 'POST':
        flash('Please enter initials', 'error')

    (current_bookings, current_owners) = kit_bookings_dict()

    return lifeguard_render('kit_bookings.html',
                            title='Kit Bookings',
                            form=form,
                            current_bookings=current_bookings)


def kit_bookings_dict():
    with open('/home/clearwater/rjp/l3dash/clearwater_kit_state.txt', 'r') as current_bookings:
        current_bookings_lines = current_bookings.readlines()
    kit_state = {}
    kit_owner = {}
    for line in current_bookings_lines:
        if len(line.split('=')) > 1:
            if line.split('=')[1].strip() == 'booked':
                kit_state[line.split('=')[0]] = True
                kit_owner[line.split('=')[0]] = line.split('=')[2].strip()
            else:
                kit_state[line.split('=')[0]] = False
    return (kit_state, kit_owner)


def book_kit(form):
    log_kit_booking(form)
    (current_bookings, current_owners) = kit_bookings_dict()
    with open('clearwater_kit_state.txt', 'w') as booking_state:
        for deployment in form.clearwater_deployments:
            for node in deployment['nodes']:
                if node.data:
                    booking_state.write(str(node.name) + '=' + 'booked' + '=' + str(form.name.data) + '\n')
                elif current_bookings[str(node.name)]:
                    booking_state.write(str(node.name) + '=' + 'booked' + '=' + current_owners[str(node.name)] + '\n')
                else:
                    booking_state.write(str(node.name) + '=' + 'unbooked' + '\n')


def log_kit_booking(form):
    with open('/home/clearwater/rjp/l3dash/clearwater_kit_bookings.log', 'w') as bookings_ledger:
        bookings_ledger.write('\nperson: ' + form.name.data)
        for deployment in form.clearwater_deployments:
            for node in deployment['nodes']:
                if node.data:
                    bookings_ledger.write('\n' + node.name)
        bookings_ledger.write('\nnote: ' + str(form.note.data))
        bookings_ledger.write('\n')
