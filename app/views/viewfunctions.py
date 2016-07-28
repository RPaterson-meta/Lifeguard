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
    'subtopics': [KIT_BOOKING, KIT_STATUS]
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
