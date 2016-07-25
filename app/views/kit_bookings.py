from app import app
from app.views.viewfunctions import lifeguard_render
from app.forms import KitBookingForm


@app.route('/kit_bookings', methods=['GET', 'POST'])
def kit_bookings():
    form = KitBookingForm()
    print(form.name.data)
    return lifeguard_render('kit_bookings.html',
                            title='Kit Bookings',
                            form=form)
