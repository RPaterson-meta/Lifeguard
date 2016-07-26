from flask_wtf import Form
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired


class KitBookingForm(Form):
    l3_cc_sprout1 = {'id': 'l3_cc_sprout1', 'name': 'Sprout 1'}
    l3_cc_sprout2 = {'id': 'l3_cc_sprout2', 'name': 'Sprout 2'}
    l3_cc_hstead1 = {'id': 'l3_cc_hstead1', 'name': 'Homestead 1'}
    l3_cc_hstead2 = {'id': 'l3_cc_hstead2', 'name': 'Homestead 2'}
    l3_cc_ralf1 = {'id': 'l3_cc_ralf1', 'name': 'Ralf 1'}
    l3_cc_ralf2 = {'id': 'l3_cc_ralf2', 'name': 'Ralf 2'}

    cc = {'nodes': [l3_cc_sprout1, l3_cc_sprout2, l3_cc_hstead1, l3_cc_hstead2, l3_cc_ralf1, l3_cc_ralf2], 'name': 'L3 CC'}
####################################################################################################################################################
    l3_cc2_sprout1 = {'id': 'l3_cc2_sprout1', 'name': 'Sprout 1'}
    l3_cc2_sprout2 = {'id': 'l3_cc2_sprout2', 'name': 'Sprout 2'}
    l3_cc2_hstead1 = {'id': 'l3_cc2_hstead1', 'name': 'Homestead 1'}
    l3_cc2_hstead2 = {'id': 'l3_cc2_hstead2', 'name': 'Homestead 2'}
    l3_cc2_ralf1 = {'id': 'l3_cc2_ralf1', 'name': 'Ralf 1'}
    l3_cc2_ralf2 = {'id': 'l3_cc2_ralf2', 'name': 'Ralf 2'}

    cc2 = {'nodes': [l3_cc2_sprout1, l3_cc2_sprout2, l3_cc2_hstead1, l3_cc2_hstead2, l3_cc2_ralf1, l3_cc2_ralf2], 'name': 'L3 CC2'}
####################################################################################################################################################
    l3_cc3_sprout1 = {'id': 'l3_cc3_sprout1', 'name': 'Sprout 1'}
    l3_cc3_sprout2 = {'id': 'l3_cc3_sprout2', 'name': 'Sprout 2'}
    l3_cc3_hstead1 = {'id': 'l3_cc3_hstead1', 'name': 'Homestead 1'}
    l3_cc3_hstead2 = {'id': 'l3_cc3_hstead2', 'name': 'Homestead 2'}
    l3_cc3_ralf1 = {'id': 'l3_cc3_ralf1', 'name': 'Ralf 1'}
    l3_cc3_ralf2 = {'id': 'l3_cc3_ralf2', 'name': 'Ralf 2'}

    cc3 = {'nodes': [l3_cc3_sprout1, l3_cc3_sprout2, l3_cc3_hstead1, l3_cc3_hstead2, l3_cc3_ralf1, l3_cc3_ralf2], 'name': 'L3 CC3'}
####################################################################################################################################################
    l3_cc4_sprout1 = {'id': 'l3_cc4_sprout1', 'name': 'Sprout 1'}
    l3_cc4_sprout2 = {'id': 'l3_cc4_sprout2', 'name': 'Sprout 2'}
    l3_cc4_hstead1 = {'id': 'l3_cc4_hstead1', 'name': 'Homestead 1'}
    l3_cc4_hstead2 = {'id': 'l3_cc4_hstead2', 'name': 'Homestead 2'}
    l3_cc4_ralf1 = {'id': 'l3_cc4_ralf1', 'name': 'Ralf 1'}
    l3_cc4_ralf2 = {'id': 'l3_cc4_ralf2', 'name': 'Ralf 2'}

    cc4 = {'nodes': [l3_cc4_sprout1, l3_cc4_sprout2, l3_cc4_hstead1, l3_cc4_hstead2, l3_cc4_ralf1, l3_cc4_ralf2], 'name': 'L3 CC4'}
####################################################################################################################################################
    name = StringField('name')
    note = TextAreaField('note')

    deployments = [cc, cc2, cc3, cc4]


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
