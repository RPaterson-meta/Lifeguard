from app import app
from flask import redirect, request, flash
from app.views.viewfunctions import lifeguard_render
from app.forms import KitBookingForm


@app.route('/kit_bookings', methods=['GET', 'POST'])
def kit_bookings():
    form = KitBookingForm()

    if request.method == 'POST' and form.name.data:
        with open('/home/clearwater/rjp/l3dash/clearwater_kit_bookings.log', 'w') as bookings:
            bookings.write('\nperson: ' + form.name.data)
            for deployment in form.clearwater_deployments:
                for node in deployment['nodes']:
                    if node.data:
                        bookings.write('\n' + node.name)
            bookings.write('\nnote: ' + str(form.note.data))
            bookings.write('\n')
            flash('Kit booked for ' + str(form.name.data), 'success')
        return redirect('/index')
    elif request.method == 'POST':
        flash('Please enter initials', 'error')
    return lifeguard_render('kit_bookings.html',
                            title='Kit Bookings',
                            form=form)
