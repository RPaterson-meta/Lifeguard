from app import app
from app.views.viewfunctions import lifeguard_render


@app.route('/lifeguards')
def lifeguards():
    return lifeguard_render('lifeguards.html',
                            title='Lifeguards')