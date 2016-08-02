from app import app
from flask import request, flash
from app.views.viewfunctions import lifeguard_render, get_kit_bookings, store_kit_bookings, update_deployment_availability
from app.forms import ClearwaterKitBookingForm, PerimetaKitBookingForm, VolteKitBookingForm


@app.route('/kit_management', methods=['GET'])
def kit_status():
    clearwater_form = ClearwaterKitBookingForm()
    perimeta_form = PerimetaKitBookingForm()
    volte_form = VolteKitBookingForm()
    bookings = get_kit_bookings()
    cc_deployment_names = sorted(bookings['clearwater'].keys())
    vt_deployment_names = sorted(bookings['volte'].keys())
    return lifeguard_render("kit_management.html",
                            title='Kit Management',
                            clearwater_form=clearwater_form,
                            perimeta_form=perimeta_form,
                            volte_form=volte_form,
                            bookings=bookings,
                            vt_deployment_names=vt_deployment_names,
                            cc_deployment_names=cc_deployment_names)
