from app import app
from app.views.viewfunctions import lifeguard_render, homepage


@app.route('/')
@app.route('/index')
def index():
    return lifeguard_render(homepage(),
                            title='Home')
