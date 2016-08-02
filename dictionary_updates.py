#!flask/bin/python
import ast
import os


def read_dictionary_from_file(afilepath):
    with open(afilepath, 'r') as afile:
        file_str = afile.read()
    return ast.literal_eval(file_str)


def get_kit_bookings():
    return read_dictionary_from_file(os.path.dirname(__file__) + '/clearwater_kit_state.txt')


def write_dictionary_to_file(input_dictionary, afilepath):
    with open(afilepath, 'w') as afile:
        afile.write(str(input_dictionary))


def store_kit_bookings(input_dictionary):
    write_dictionary_to_file(input_dictionary, os.path.dirname(
        __file__) + '/clearwater_kit_state.txt')


if __name__ == '__main__':
    bookings = get_kit_bookings()

    l3_vt2_dcm1 = {'name': 'l3_vt2_dcm1', 'available': True, 'tooltip': ''}
    l3_vt2_dcm2 = {'name': 'l3_vt2_dcm2', 'available': True, 'tooltip': ''}
    l3_vt2_hstead1 = {'name': 'l3_vt2_hstead1',
                      'available': True, 'tooltip': ''}
    l3_vt2_hstead2 = {'name': 'l3_vt2_hstead2',
                      'available': True, 'tooltip': ''}
    l3_vt2_ip_sm_gw1 = {'name': 'l3_vt2_ip_sm_gw1',
                        'available': True, 'tooltip': ''}
    l3_vt2_mrf1 = {'name': 'l3_vt2_mrf1', 'available': True, 'tooltip': ''}
    l3_vt2_perim1 = {'name': 'l3_vt2_perim1', 'available': True, 'tooltip': ''}
    l3_vt2_rem_ag1 = {'name': 'l3_vt2_rem_ag1',
                      'available': True, 'tooltip': ''}
    l3_vt2_sg1 = {'name': 'l3_vt2_sg1', 'available': True, 'tooltip': ''}
    l3_vt2_sprout1 = {'name': 'l3_vt2_sprout1',
                      'available': True, 'tooltip': ''}
    l3_vt2_sprout2 = {'name': 'l3_vt2_sprout2',
                      'available': True, 'tooltip': ''}
    l3_vt2_tas1 = {'name': 'l3_vt2_tas1', 'available': True, 'tooltip': ''}

    l3_vt2 = {'name': 'l3_vt2',
              'nodes': {'l3_vt2_dcm1': l3_vt2_dcm1,
                        'l3_vt2_dcm2': l3_vt2_dcm2,
                        'l3_vt2_hstead1': l3_vt2_hstead1,
                        'l3_vt2_hstead2': l3_vt2_hstead2,
                        'l3_vt2_ip_sm_gw1': l3_vt2_ip_sm_gw1,
                        'l3_vt2_mrf1': l3_vt2_mrf1,
                        'l3_vt2_perim1': l3_vt2_perim1,
                        'l3_vt2_rem_ag1': l3_vt2_rem_ag1,
                        'l3_vt2_sg1': l3_vt2_sg1,
                        'l3_vt2_sprout1': l3_vt2_sprout1,
                        'l3_vt2_sprout2': l3_vt2_sprout2,
                        'l3_vt2_tas1': l3_vt2_tas1},
              'fully_unbooked': True,
              'fully_booked': False,
              'state': 'success'}

    bookings['volte']['l3_vt2'] = l3_vt2
    store_kit_bookings(bookings)
