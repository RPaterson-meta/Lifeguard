from flask_wtf import Form
from wtforms import StringField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class ClearwaterKitBookingForm(Form):
    name = StringField('name')
    note = TextAreaField('note')

    l3_cc_sprout1 = BooleanField('l3_cc_sprout1', default=False)
    l3_cc_sprout2 = BooleanField('l3_cc_sprout2', default=False)
    l3_cc_hstead1 = BooleanField('l3_cc_hstead1', default=False)
    l3_cc_hstead2 = BooleanField('l3_cc_hstead2', default=False)
    l3_cc_ralf1 = BooleanField('l3_cc_ralf1', default=False)
    l3_cc_ralf2 = BooleanField('l3_cc_ralf2', default=False)

##########################################################################
    l3_cc2_sprout1 = BooleanField('l3_cc2_sprout1', default=False)
    l3_cc2_sprout2 = BooleanField('l3_cc2_sprout2', default=False)
    l3_cc2_hstead1 = BooleanField('l3_cc2_hstead1', default=False)
    l3_cc2_hstead2 = BooleanField('l3_cc2_hstead2', default=False)
    l3_cc2_ralf1 = BooleanField('l3_cc2_ralf1', default=False)
    l3_cc2_ralf2 = BooleanField('l3_cc2_ralf2', default=False)

##########################################################################
    l3_cc3_sprout1 = BooleanField('l3_cc3_sprout1', default=False)
    l3_cc3_sprout2 = BooleanField('l3_cc3_sprout2', default=False)
    l3_cc3_sprout3 = BooleanField('l3_cc3_sprout3', default=False)
    l3_cc3_hstead1 = BooleanField('l3_cc3_hstead1', default=False)
    l3_cc3_hstead2 = BooleanField('l3_cc3_hstead2', default=False)
    l3_cc3_hstead3 = BooleanField('l3_cc3_hstead3', default=False)
    l3_cc3_ralf1 = BooleanField('l3_cc3_ralf1', default=False)
    l3_cc3_ralf2 = BooleanField('l3_cc3_ralf2', default=False)

##########################################################################
    l3_cc4_sprout1 = BooleanField('l3_cc4_sprout1', default=False)
    l3_cc4_sprout2 = BooleanField('l3_cc4_sprout2', default=False)
    l3_cc4_hstead1 = BooleanField('l3_cc4_hstead1', default=False)
    l3_cc4_hstead2 = BooleanField('l3_cc4_hstead2', default=False)
    l3_cc4_ralf1 = BooleanField('l3_cc4_ralf1', default=False)
    l3_cc4_ralf2 = BooleanField('l3_cc4_ralf2', default=False)

##########################################################################

    @property
    def form_nodes(self):
        return [self.l3_cc_sprout1,
                self.l3_cc_sprout2,
                self.l3_cc_hstead1,
                self.l3_cc_hstead2,
                self.l3_cc_ralf1,
                self.l3_cc_ralf2,
                self.l3_cc2_sprout1,
                self.l3_cc2_sprout2,
                self.l3_cc2_hstead1,
                self.l3_cc2_hstead2,
                self.l3_cc2_ralf1,
                self.l3_cc2_ralf2,
                self.l3_cc3_sprout1,
                self.l3_cc3_sprout2,
                self.l3_cc3_sprout3,
                self.l3_cc3_hstead1,
                self.l3_cc3_hstead2,
                self.l3_cc3_hstead3,
                self.l3_cc3_ralf1,
                self.l3_cc3_ralf2,
                self.l3_cc4_sprout1,
                self.l3_cc4_sprout2,
                self.l3_cc4_hstead1,
                self.l3_cc4_hstead2,
                self.l3_cc4_ralf1,
                self.l3_cc4_ralf2]

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
    def deployments(self):
        return [self.cc, self.cc2, self.cc3, self.cc4]


class PerimetaKitBookingForm(Form):
    l3_cc_perim1 = BooleanField('l3_cc_perim1', default=False)
    name = StringField('perimeta_name')
    pointing = SelectField('Select Deployment', choices=[('Select Deployment', 'Select Deployment'), ('l3-cc', 'l3_cc'), ('l3-cc2', 'l3_cc2'), ('l3-cc3', 'l3_cc3'), ('l3-cc4', 'l3_cc4')])
    note = TextAreaField('perimeta_note')
    use_pointing = BooleanField('use_perim', default=False)

    @property
    def perimeta_instances(self):
        return {'name': 'Perimeta', 'nodes': [self.l3_cc_perim1]}


class VolteKitBookingForm(Form):
    name = StringField('name')
    note = TextAreaField('note')

    l3_vt_dcm1 = BooleanField('l3_vt_dcm1', default=False)
    l3_vt_dcm2 = BooleanField('l3_vt_dcm2', default=False)
    l3_vt_hstead1 = BooleanField('l3_vt_hstead1', default=False)
    l3_vt_hstead2 = BooleanField('l3_vt_hstead2', default=False)
    l3_vt_ip_sm_gw1 = BooleanField('l3_vt_ip_sm_gw1', default=False)
    l3_vt_mrf1 = BooleanField('l3_vt_mrf1', default=False)
    l3_vt_perim1 = BooleanField('l3_vt_perim1', default=False)
    l3_vt_rem_ag1 = BooleanField('l3_vt_rem_ag1', default=False)
    l3_vt_sg1 = BooleanField('l3_vt_sg1', default=False)
    l3_vt_sprout1 = BooleanField('l3_vt_sprout1', default=False)
    l3_vt_sprout2 = BooleanField('l3_vt_sprout2', default=False)
    l3_vt_tas1 = BooleanField('l3_vt_tas1', default=False)

##########################################################################

    @property
    def form_nodes(self):
        return [self.l3_vt_dcm1,
                self.l3_vt_dcm2,
                self.l3_vt_hstead1,
                self.l3_vt_hstead2,
                self.l3_vt_ip_sm_gw1,
                self.l3_vt_mrf1,
                self.l3_vt_perim1,
                self.l3_vt_rem_ag1,
                self.l3_vt_sg1,
                self.l3_vt_sprout1,
                self.l3_vt_sprout2,
                self.l3_vt_tas1]

    @property
    def vt(self):
        return {'name': 'l3_vt', 'nodes': [self.l3_vt_dcm1, self.l3_vt_dcm2, self.l3_vt_hstead1, self.l3_vt_hstead2, self.l3_vt_ip_sm_gw1, self.l3_vt_mrf1, self.l3_vt_perim1, self.l3_vt_rem_ag1, self.l3_vt_sg1, self.l3_vt_sprout1, self.l3_vt_sprout2, self.l3_vt_tas1]}

    @property
    def deployments(self):
        return [self.vt]


class CCFKitBookingForm(Form):
    name = StringField('name')
    note = TextAreaField('note')

    l3_ccf1_cedar1 = BooleanField('l3_ccf1_cedar1', default=False)
    l3_ccf1_cedar2 = BooleanField('l3_ccf1_cedar2', default=False)
    l3_ccf1_cedar3 = BooleanField('l3_ccf1_cedar3', default=False)

##########################################################################

    @property
    def form_nodes(self):
        return [self.l3_ccf1_cedar1,
                self.l3_ccf1_cedar2,
                self.l3_ccf1_cedar3]

    @property
    def ccf1(self):
        return {'name': 'l3_ccf1', 'nodes': [self.l3_ccf1_cedar1,
                                             self.l3_ccf1_cedar2,
                                             self.l3_ccf1_cedar3]}

    @property
    def deployments(self):
        return [self.ccf1]


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
