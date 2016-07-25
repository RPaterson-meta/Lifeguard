from app import app
from app.views.viewfunctions import lifeguard_render


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    return lifeguard_render("index.html",
                            title='Home',
                            user=user)
