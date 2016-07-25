from flask import render_template
##########################################################################
# SUBTOPICS
###########
# ORCHESTRATION
MANAGE_NODES = {'name': 'Manage Nodes',
                'location': '/#'
                }
KIT_BOOKINGS = {'name': 'Kit Bookings',
                'location': '/kit_bookings'
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
    'subtopics': [KIT_BOOKINGS]
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

################################################################################
# HEADINGS
##########
HEADINGS = [ORCHESTRATION, TEAM, BUILDS, ISSUES]


def lifeguard_render(*args, **kwargs):
    return render_template(*args, head_links=HEADINGS, **kwargs)
