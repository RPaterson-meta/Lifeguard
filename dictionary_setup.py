#!flask/bin/python
def write_dictionary_to_file(input_dictionary, afilepath):
    with open(afilepath, 'w') as afile:
        afile.write(str(input_dictionary))


if __name__ == '__main__':

    # Clearwater
    l3_cc_sprout1 = {'name': 'l3_cc_sprout1', 'available': True, 'tooltip': ''}
    l3_cc_sprout2 = {'name': 'l3_cc_sprout2', 'available': True, 'tooltip': ''}
    l3_cc_hstead1 = {'name': 'l3_cc_hstead1', 'available': True, 'tooltip': ''}
    l3_cc_hstead2 = {'name': 'l3_cc_hstead2', 'available': True, 'tooltip': ''}
    l3_cc_ralf1 = {'name': 'l3_cc_ralf1', 'available': True, 'tooltip': ''}
    l3_cc_ralf2 = {'name': 'l3_cc_ralf2', 'available': True, 'tooltip': ''}

    l3_cc2_sprout1 = {'name': 'l3_cc2_sprout1',
                      'available': True, 'tooltip': ''}
    l3_cc2_sprout2 = {'name': 'l3_cc2_sprout2',
                      'available': True, 'tooltip': ''}
    l3_cc2_hstead1 = {'name': 'l3_cc2_hstead1',
                      'available': True, 'tooltip': ''}
    l3_cc2_hstead2 = {'name': 'l3_cc2_hstead2',
                      'available': True, 'tooltip': ''}
    l3_cc2_ralf1 = {'name': 'l3_cc2_ralf1', 'available': True, 'tooltip': ''}
    l3_cc2_ralf2 = {'name': 'l3_cc2_ralf2', 'available': True, 'tooltip': ''}

    l3_cc3_sprout1 = {'name': 'l3_cc3_sprout1',
                      'available': True, 'tooltip': ''}
    l3_cc3_sprout2 = {'name': 'l3_cc3_sprout2',
                      'available': True, 'tooltip': ''}
    l3_cc3_sprout3 = {'name': 'l3_cc3_sprout3',
                      'available': True, 'tooltip': ''}
    l3_cc3_hstead1 = {'name': 'l3_cc3_hstead1',
                      'available': True, 'tooltip': ''}
    l3_cc3_hstead2 = {'name': 'l3_cc3_hstead2',
                      'available': True, 'tooltip': ''}
    l3_cc3_hstead3 = {'name': 'l3_cc3_hstead3',
                      'available': True, 'tooltip': ''}
    l3_cc3_ralf1 = {'name': 'l3_cc3_ralf1', 'available': True, 'tooltip': ''}
    l3_cc3_ralf2 = {'name': 'l3_cc3_ralf2', 'available': True, 'tooltip': ''}

    l3_cc4_sprout1 = {'name': 'l3_cc4_sprout1',
                      'available': True, 'tooltip': ''}
    l3_cc4_sprout2 = {'name': 'l3_cc4_sprout2',
                      'available': True, 'tooltip': ''}
    l3_cc4_hstead1 = {'name': 'l3_cc4_hstead1',
                      'available': True, 'tooltip': ''}
    l3_cc4_hstead2 = {'name': 'l3_cc4_hstead2',
                      'available': True, 'tooltip': ''}
    l3_cc4_ralf1 = {'name': 'l3_cc4_ralf1', 'available': True, 'tooltip': ''}
    l3_cc4_ralf2 = {'name': 'l3_cc4_ralf2', 'available': True, 'tooltip': ''}

    cc = {'name': 'l3_cc',
          'nodes': {'l3_cc_sprout1': l3_cc_sprout1,
                    'l3_cc_sprout2': l3_cc_sprout2,
                    'l3_cc_hstead1': l3_cc_hstead1,
                    'l3_cc_hstead2': l3_cc_hstead2,
                    'l3_cc_ralf1': l3_cc_ralf1,
                    'l3_cc_ralf2': l3_cc_ralf2},
          'fully_unbooked': True,
          'fully_booked': False,
          'state': 'success'}
    cc2 = {'name': 'l3_cc2',
           'nodes': {'l3_cc2_sprout1': l3_cc2_sprout1,
                     'l3_cc2_sprout2': l3_cc2_sprout2,
                     'l3_cc2_hstead1': l3_cc2_hstead1,
                     'l3_cc2_hstead2': l3_cc2_hstead2,
                     'l3_cc2_ralf1': l3_cc2_ralf1,
                     'l3_cc2_ralf2': l3_cc2_ralf2},
           'fully_unbooked': True,
           'fully_booked': False,
           'state': 'success'}
    cc3 = {'name': 'l3_cc3',
           'nodes': {'l3_cc3_sprout1': l3_cc3_sprout1,
                     'l3_cc3_sprout2': l3_cc3_sprout2,
                     'l3_cc3_sprout3': l3_cc3_sprout3,
                     'l3_cc3_hstead1': l3_cc3_hstead1,
                     'l3_cc3_hstead2': l3_cc3_hstead2,
                     'l3_cc3_hstead3': l3_cc3_hstead3,
                     'l3_cc3_ralf1': l3_cc3_ralf1,
                     'l3_cc3_ralf2': l3_cc3_ralf2},
           'fully_unbooked': True,
           'fully_booked': False,
           'state': 'success'}
    cc4 = {'name': 'l3_cc4',
           'nodes': {'l3_cc4_sprout1': l3_cc4_sprout1,
                     'l3_cc4_sprout2': l3_cc4_sprout2,
                     'l3_cc4_hstead1': l3_cc4_hstead1,
                     'l3_cc4_hstead2': l3_cc4_hstead2,
                     'l3_cc4_ralf1': l3_cc4_ralf1,
                     'l3_cc4_ralf2': l3_cc4_ralf2},
           'fully_unbooked': True,
           'fully_booked': False,
           'state': 'success'}
    clearwater = {'l3_cc': cc, 'l3_cc2': cc2, 'l3_cc3': cc3, 'l3_cc4': cc4}

    # VoLTE
    l3_vt_dcm1 = {'name': 'l3_vt_dcm1', 'available': True, 'tooltip': ''}
    l3_vt_dcm2 = {'name': 'l3_vt_dcm2', 'available': True, 'tooltip': ''}
    l3_vt_hstead1 = {'name': 'l3_vt_hstead1', 'available': True, 'tooltip': ''}
    l3_vt_hstead2 = {'name': 'l3_vt_hstead2', 'available': True, 'tooltip': ''}
    l3_vt_ip_sm_gw1 = {'name': 'l3_vt_ip_sm_gw1',
                       'available': True, 'tooltip': ''}
    l3_vt_mrf1 = {'name': 'l3_vt_mrf1', 'available': True, 'tooltip': ''}
    l3_vt_perim1 = {'name': 'l3_vt_perim1', 'available': True, 'tooltip': ''}
    l3_vt_dcm1 = {'name': 'l3_vt_dcm1', 'available': True, 'tooltip': ''}
    l3_vt_rem_ag1 = {'name': 'l3_vt_rem_ag1', 'available': True, 'tooltip': ''}
    l3_vt_sg1 = {'name': 'l3_vt_sg1', 'available': True, 'tooltip': ''}
    l3_vt_sprout1 = {'name': 'l3_vt_sprout1', 'available': True, 'tooltip': ''}
    l3_vt_sprout2 = {'name': 'l3_vt_sprout2', 'available': True, 'tooltip': ''}
    l3_vt_tas1 = {'name': 'l3_vt_tas1', 'available': True, 'tooltip': ''}

    l3_vt = {'name': 'l3_vt',
             'nodes': {'l3_vt_dcm1': l3_vt_dcm1,
                       'l3_vt_dcm2': l3_vt_dcm2,
                       'l3_vt_hstead1': l3_vt_hstead1,
                       'l3_vt_hstead2': l3_vt_hstead2,
                       'l3_vt_ip_sm_gw1': l3_vt_ip_sm_gw1,
                       'l3_vt_mrf1': l3_vt_mrf1,
                       'l3_vt_perim1': l3_vt_perim1,
                       'l3_vt_dcm1': l3_vt_dcm1,
                       'l3_vt_rem_ag1': l3_vt_rem_ag1,
                       'l3_vt_sg1': l3_vt_sg1,
                       'l3_vt_sprout1': l3_vt_sprout1,
                       'l3_vt_sprout2': l3_vt_sprout2,
                       'l3_vt_tas1': l3_vt_tas1},
             'fully_unbooked': True,
             'fully_booked': False,
             'state': 'success'}
    volte = {'l3_vt': l3_vt}

    bookings = {"clearwater": clearwater, 'volte': volte}
    write_dictionary_to_file(
        bookings, '/home/clearwater/rjp/l3dash/clearwater_kit_state.txt')
