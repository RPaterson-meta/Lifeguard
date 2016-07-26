from app import app
from flask import redirect, request
from app.views.viewfunctions import lifeguard_render
from app.forms import KitBookingForm


@app.route('/kit_bookings', methods=['GET', 'POST'])
def kit_bookings():
    form = KitBookingForm()
    print(form.name.data)
    if request.method == 'POST' and form.name.data:
        with open('/home/clearwater/rjp/l3dash/Kit_bookings.log', 'w') as bookings:
            bookings.write('\nperson: ' + form.name.data)
            bookings.write('\nnote: ' + form.note.data)
        return redirect('/index')
    return lifeguard_render('kit_bookings.html',
                            title='Kit Bookings',
                            form=form)
