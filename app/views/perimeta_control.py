from app import app
from flask import request, flash
from app.views.viewfunctions import lifeguard_render, get_kit_bookings, store_kit_bookings, update_deployment_availability
from app.forms import PerimetaKitBookingForm


@app.route('/perimeta_control', methods=['GET', 'POST'])
def perimeta_control():
    # Clever Python stuff goes here
    return lifeguard_render("perimeta_control.html")
