from flask import render_template
import ast
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
KIT_STATUS = {'name': 'Kit Status',
              'location': '/kit_status'
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
    write_dictionary_to_file(input_dictionary, '/home/clearwater/rjp/l3dash/clearwater_kit_state.txt')


def get_kit_bookings():
    return read_dictionary_from_file('/home/clearwater/rjp/l3dash/clearwater_kit_state.txt')


def update_deployment_availability(deployment, bookings):
    node_availability = []
    for node in deployment['nodes']:
        node_availability.append(bookings[deployment['name']]['nodes'][node.name]['available'])

    bookings[deployment['name']]['fully_unbooked'] = False not in node_availability
    bookings[deployment['name']]['fully_booked'] = True not in node_availability

    has_some_available = True in node_availability

    if bookings[deployment['name']]['fully_unbooked']:
        bookings[deployment['name']]['state'] = 'success'
    elif has_some_available:
        bookings[deployment['name']]['state'] = 'warning'
    else:
        bookings[deployment['name']]['state'] = 'danger'
