from flask import render_template
##########################################################################
# SUBTOPICS
###########
MANAGE_NODES = {'name': 'Manage Nodes',
                'location': '/#'
                }
KIT_BOOKINGS = {'name': 'Kit Bookings',
                'location': '/kit_bookings'
                }
WHEREABOUTS = {'name': 'Whereabouts',
               'location': '/whereabouts'
               }
WORKLOAD = {'name': 'Workload',
            'location': '/#'
            }
NAUGHTY_BOARD = {'name': 'Naughty Board',
                 'location': '/#'
                 }
OVERNIGHT_BUILD = {'name': 'Overnight Build',
                   'location': '/#'
                   }
CREATE_BUILD = {'name': 'Create Build',
                'location': '/#'
                }
CHANGELOGS = {'name': 'Changelogs',
              'location': '/#'
              }
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
    'subtopics': [MANAGE_NODES, KIT_BOOKINGS]
}

TEAM = {
    'name': 'Team',
    'subtopics': [WHEREABOUTS, WORKLOAD, NAUGHTY_BOARD]
}

BUILDS = {
    'name': 'Builds',
    'subtopics': [OVERNIGHT_BUILD, CREATE_BUILD, CHANGELOGS]
}

ISSUES = {
    'name': 'Issues',
    'subtopics': [OPEN_ISSUES, PENDING_ISSUES]
}

################################################################################
# HEADINGS
##########
HEADINGS = [ORCHESTRATION, TEAM, BUILDS, ISSUES]


def lifeguard_render(*args, **kwargs):
    return render_template(*args, head_links=HEADINGS, **kwargs)
