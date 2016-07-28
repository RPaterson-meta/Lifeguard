from flask_wtf import Form
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired


class KitBookingForm(Form):
    name = StringField('name')
    note = TextAreaField('note')

    l3_cc_sprout1 = BooleanField('l3_cc_sprout1', default=False)
    l3_cc_sprout2 = BooleanField('l3_cc_sprout2', default=False)
    l3_cc_hstead1 = BooleanField('l3_cc_hstead1', default=False)
    l3_cc_hstead2 = BooleanField('l3_cc_hstead2', default=False)
    l3_cc_ralf1 = BooleanField('l3_cc_ralf1', default=False)
    l3_cc_ralf2 = BooleanField('l3_cc_ralf2', default=False)

####################################################################################################################################################
    l3_cc2_sprout1 = BooleanField('l3_cc2_sprout1', default=False)
    l3_cc2_sprout2 = BooleanField('l3_cc2_sprout2', default=False)
    l3_cc2_hstead1 = BooleanField('l3_cc2_hstead1', default=False)
    l3_cc2_hstead2 = BooleanField('l3_cc2_hstead2', default=False)
    l3_cc2_ralf1 = BooleanField('l3_cc2_ralf1', default=False)
    l3_cc2_ralf2 = BooleanField('l3_cc2_ralf2', default=False)

####################################################################################################################################################
    l3_cc3_sprout1 = BooleanField('l3_cc3_sprout1', default=False)
    l3_cc3_sprout2 = BooleanField('l3_cc3_sprout2', default=False)
    l3_cc3_sprout3 = BooleanField('l3_cc3_sprout3', default=False)
    l3_cc3_hstead1 = BooleanField('l3_cc3_hstead1', default=False)
    l3_cc3_hstead2 = BooleanField('l3_cc3_hstead2', default=False)
    l3_cc3_hstead3 = BooleanField('l3_cc3_hstead3', default=False)
    l3_cc3_ralf1 = BooleanField('l3_cc3_ralf1', default=False)
    l3_cc3_ralf2 = BooleanField('l3_cc3_ralf2', default=False)

####################################################################################################################################################
    l3_cc4_sprout1 = BooleanField('l3_cc4_sprout1', default=False)
    l3_cc4_sprout2 = BooleanField('l3_cc4_sprout2', default=False)
    l3_cc4_hstead1 = BooleanField('l3_cc4_hstead1', default=False)
    l3_cc4_hstead2 = BooleanField('l3_cc4_hstead2', default=False)
    l3_cc4_ralf1 = BooleanField('l3_cc4_ralf1', default=False)
    l3_cc4_ralf2 = BooleanField('l3_cc4_ralf2', default=False)

####################################################################################################################################################

    @property
    def cc(self):
        return {'name': 'l3_cc', 'nodes': [self.l3_cc_sprout1, self.l3_cc_sprout2, self.l3_cc_hstead1, self.l3_cc_hstead2, self.l3_cc_ralf1, self.l3_cc_ralf2]}

    @property
    def cc2(self):
        return {'name': 'l3_cc2', 'nodes': [self.l3_cc2_sprout1, self.l3_cc2_sprout2, self.l3_cc2_hstead1, self.l3_cc2_hstead2, self.l3_cc2_ralf1, self.l3_cc2_ralf2]}

    @property
    def cc3(self):
        return {'name': 'l3_cc3', 'nodes': [self.l3_cc3_sprout1, self.l3_cc3_sprout2, self.l3_cc3_sprout3, self.l3_cc3_hstead1, self.l3_cc3_hstead2, self.l3_cc3_hstead3, self.l3_cc3_ralf1, self.l3_cc3_ralf2]}

    @property
    def cc4(self):
        return {'name': 'l3_cc4', 'nodes': [self.l3_cc4_sprout1, self.l3_cc4_sprout2, self.l3_cc4_hstead1, self.l3_cc4_hstead2, self.l3_cc4_ralf1, self.l3_cc4_ralf2]}

    @property
    def clearwater_deployments(self):
        return [self.cc, self.cc2, self.cc3, self.cc4]


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
