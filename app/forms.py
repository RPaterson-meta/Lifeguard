from flask_wtf import Form
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired


class KitBookingForm(Form):
    l3_cc4_sprout1 = BooleanField('l3_cc4_sprout1', default=False)
    l3_cc4_sprout2 = BooleanField('l3_cc4_sprout2', default=False)
    l3_cc4_hstead1 = BooleanField('l3_cc4_hstead1', default=False)
    l3_cc4_hstead2 = BooleanField('l3_cc4_hstead2', default=False)
    l3_cc4_ralf1 = BooleanField('l3_cc4_ralf1', default=False)
    l3_cc4_ralf2 = BooleanField('l3_cc4_ralf2', default=False)
    name = StringField('name', validators=[DataRequired()])
    note = TextAreaField('note', validators=[DataRequired()])



class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
