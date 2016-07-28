#!flask/bin/python
def write_dictionary_to_file(input_dictionary, afilepath):
    with open(afilepath, 'w') as afile:
        afile.write(str(input_dictionary))


if __name__ == '__main__':
    l3_cc_sprout1 = {'name': 'l3_cc_sprout1', 'available': True}
    l3_cc_sprout2 = {'name': 'l3_cc_sprout2', 'available': True}
    l3_cc_hstead1 = {'name': 'l3_cc_hstead1', 'available': True}
    l3_cc_hstead2 = {'name': 'l3_cc_hstead2', 'available': True}
    l3_cc_ralf1 = {'name': 'l3_cc_ralf1', 'available': True}
    l3_cc_ralf2 = {'name': 'l3_cc_ralf2', 'available': True}

    l3_cc2_sprout1 = {'name': 'l3_cc2_sprout1', 'available': True}
    l3_cc2_sprout2 = {'name': 'l3_cc2_sprout2', 'available': True}
    l3_cc2_hstead1 = {'name': 'l3_cc2_hstead1', 'available': True}
    l3_cc2_hstead2 = {'name': 'l3_cc2_hstead2', 'available': True}
    l3_cc2_ralf1 = {'name': 'l3_cc2_ralf1', 'available': True}
    l3_cc2_ralf2 = {'name': 'l3_cc2_ralf2', 'available': True}

    l3_cc3_sprout1 = {'name': 'l3_cc3_sprout1', 'available': True}
    l3_cc3_sprout2 = {'name': 'l3_cc3_sprout2', 'available': True}
    l3_cc3_sprout3 = {'name': 'l3_cc3_sprout3', 'available': True}
    l3_cc3_hstead1 = {'name': 'l3_cc3_hstead1', 'available': True}
    l3_cc3_hstead2 = {'name': 'l3_cc3_hstead2', 'available': True}
    l3_cc3_hstead3 = {'name': 'l3_cc3_hstead3', 'available': True}
    l3_cc3_ralf1 = {'name': 'l3_cc3_ralf1', 'available': True}
    l3_cc3_ralf2 = {'name': 'l3_cc3_ralf2', 'available': True}

    l3_cc4_sprout1 = {'name': 'l3_cc4_sprout1', 'available': True}
    l3_cc4_sprout2 = {'name': 'l3_cc4_sprout2', 'available': True}
    l3_cc4_hstead1 = {'name': 'l3_cc4_hstead1', 'available': True}
    l3_cc4_hstead2 = {'name': 'l3_cc4_hstead2', 'available': True}
    l3_cc4_ralf1 = {'name': 'l3_cc4_ralf1', 'available': True}
    l3_cc4_ralf2 = {'name': 'l3_cc4_ralf2', 'available': True}

    cc = {'name': 'l3_cc',
          'nodes': {'l3_cc_sprout1': l3_cc_sprout1,
                    'l3_cc_sprout2': l3_cc_sprout2,
                    'l3_cc_hstead1': l3_cc_hstead1,
                    'l3_cc_hstead2': l3_cc_hstead2,
                    'l3_cc_ralf1': l3_cc_ralf1,
                    'l3_cc_ralf2': l3_cc_ralf2},
          'available': True,
          'state': 'success'}
    cc2 = {'name': 'l3_cc2',
           'nodes': {'l3_cc2_sprout1': l3_cc2_sprout1,
                     'l3_cc2_sprout2': l3_cc2_sprout2,
                     'l3_cc2_hstead1': l3_cc2_hstead1,
                     'l3_cc2_hstead2': l3_cc2_hstead2,
                     'l3_cc2_ralf1': l3_cc2_ralf1,
                     'l3_cc2_ralf2': l3_cc2_ralf2},
           'available': True,
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
           'available': True,
           'state': 'success'}
    cc4 = {'name': 'l3_cc4',
           'nodes': {'l3_cc4_sprout1': l3_cc4_sprout1,
                     'l3_cc4_sprout2': l3_cc4_sprout2,
                     'l3_cc4_hstead1': l3_cc4_hstead1,
                     'l3_cc4_hstead2': l3_cc4_hstead2,
                     'l3_cc4_ralf1': l3_cc4_ralf1,
                     'l3_cc4_ralf2': l3_cc4_ralf2},
           'available': True,
           'state': 'success'}
    bookings = {'l3_cc': cc, 'l3_cc2': cc2, 'l3_cc3': cc3, 'l3_cc4': cc4}
    write_dictionary_to_file(bookings, '/home/clearwater/rjp/l3dash/clearwater_kit_state.txt')
