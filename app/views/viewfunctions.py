from flask import render_template
import ast
import paramiko
import os
import datetime
from subprocess import check_output
##########################################################################
# SUBTOPICS
###########
# ORCHESTRATION
MANAGE_NODES = {'name': 'Manage Nodes',
                'location': '/#'
                }
KIT_BOOKING = {'name': 'Kit Booking',
               'location': '/kit_booking'
               }
KIT_STATUS = {'name': 'Kit Management',
              'location': '/kit_management'
              }
#################
# TEAM
WHEREABOUTS = {'name': 'Whereabouts',
               'location': '/whereabouts'
               }
WORKLOAD = {'name': 'Workload',
            'location': '/#'
            }
NAUGHTY_BOARD = {'name': 'Naughty Board',
                 'location': '/#'
                 }
##################
# BUILDS
OVERNIGHT_BUILD = {'name': 'Overnight Build',
                   'location': '/#'
                   }
CREATE_BUILD = {'name': 'Create Build',
                'location': '/#'
                }
CHANGELOGS = {'name': 'Changelogs',
              'location': '/#'
              }
###############
# ISSUES
OPEN_ISSUES = {'name': 'Open Issues',
               'location': '/#'
               }
PENDING_ISSUES = {'name': 'Pending Issues',
                  'location': '/#'
                  }

##########################################################################
# TOPICS
########
ORCHESTRATION = {
    'name': 'Orchestration',
    'subtopics': [KIT_STATUS]
}

TEAM = {
    'name': 'Team',
    'subtopics': [WHEREABOUTS]
}

BUILDS = {
    'name': 'Builds',
    'subtopics': []
}

ISSUES = {
    'name': 'Issues',
    'subtopics': []
}

##########################################################################
# HEADINGS
##########
HEADINGS = [ORCHESTRATION, TEAM, BUILDS, ISSUES]


def lifeguard_render(*args, **kwargs):
    return render_template(*args, head_links=HEADINGS, **kwargs)


def write_dictionary_to_file(input_dictionary, afilepath):
    with open(afilepath, 'w') as afile:
        afile.write(str(input_dictionary))


def read_dictionary_from_file(afilepath):
    with open(afilepath, 'r') as afile:
        file_str = afile.read()
    return ast.literal_eval(file_str)


def store_kit_bookings(input_dictionary):
    write_dictionary_to_file(input_dictionary, os.path.dirname(
        __file__) + '/../../clearwater_kit_state.txt')


def get_kit_bookings():
    return read_dictionary_from_file(os.path.dirname(__file__) + '/../../clearwater_kit_state.txt')


def update_deployment_availability(product, deployment, bookings):
    node_availability = []
    for node in deployment['nodes']:
        node_availability.append(bookings[product][deployment['name']][
                                 'nodes'][node.name]['available'])

    bookings[product][deployment['name']][
        'fully_unbooked'] = False not in node_availability
    bookings[product][deployment['name']][
        'fully_booked'] = True not in node_availability

    has_some_available = True in node_availability

    if bookings[product][deployment['name']]['fully_unbooked']:
        bookings[product][deployment['name']]['state'] = 'success'
    elif has_some_available:
        bookings[product][deployment['name']]['state'] = 'warning'
    else:
        bookings[product][deployment['name']]['state'] = 'danger'


def point_perimeta(name):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('l3-cc-perim1.datcon.co.uk', username='root',
                   password='!bootstrap')
    client.exec_command('echo \'Lifeguard is pointing perimeta\' | wall')
    ip = nslookup(name + '-sprout1')
    print('executing command \n\n' + '/root/point_perim.sh ' + ip + '\n\n')
    client.exec_command('/root/point_perim.sh ' + ip)
    client.close()


def nslookup(name):
    ns_output = check_output('nslookup ' + name, shell=True).decode()
    ns_lines = ns_output.split('\n')
    ns_lines = [line for line in ns_lines if 'Address:' in line]
    ns_lines = list(ns_lines)
    ip = ns_lines[1].split(':')[1].strip()
    return ip


def homepage():
    if datetime.datetime.today().strftime('%d/%m') == '23/04':
        return '.egg/do_not_open.html'
    else:
        return 'index.html'
