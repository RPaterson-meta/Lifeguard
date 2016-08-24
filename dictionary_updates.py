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
    l3_ccf1_cedar1 = {'name': 'l3_ccf1_cedar1', 'available': True, 'tooltip': ''}
    l3_ccf1_cedar2 = {'name': 'l3_ccf1_cedar2', 'available': True, 'tooltip': ''}
    l3_ccf1_cedar3 = {'name': 'l3_ccf1_cedar3', 'available': True, 'tooltip': ''}

    l3_ccf1 = {'name': 'l3_ccf1',
               'nodes': {'l3_ccf1_cedar1': l3_ccf1_cedar1,
                         'l3_ccf1_cedar2': l3_ccf1_cedar2,
                         'l3_ccf1_cedar3': l3_ccf1_cedar3},
               'fully_unbooked': True,
               'fully_booked': False,
               'state': 'success'}
    ccf = {'l3_ccf1': l3_ccf1}
    bookings['ccf'] = ccf
    store_kit_bookings(bookings)
