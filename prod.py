import os

# Server Specific Configurations
server = {
    'port': os.environ.get('PULPITO_SERVER_PORT', '8081'),
    'host': os.environ.get('PULPITO_SERVER_HOST', '172.23.232.5')
}

# In the ceph-cm-ansible pulpito role the setup_pulpito task
# replaces last occurance of 'paddles_address' assignment
# using regex, that is why it should be one line expression.

# paddles_address = 'http://sentry.front.sepia.ceph.com:8080'
# paddles_address = os.environ.get('PULPITO_PADDLES_ADDRESS', paddles_address)
paddles_address = os.environ.get('PULPITO_PADDLES_ADDRESS', 'http://172.23.232.5:8080')

# Pecan Application Configurations
app = {
    'root': 'pulpito.controllers.root.RootController',
    'modules': ['pulpito'],
    'static_root': '%(confdir)s/public',
    'template_path': '%(confdir)s/pulpito/templates',
    'default_renderer': 'jinja',
    'guess_content_type_from_ext': False,
    'debug': True,
    'errors': {
        404: '/error/404',
        '__force_dict__': True
    }
}

logging = {
    'loggers': {
        'root': {'level': 'INFO', 'handlers': ['console']},
        'pulpito': {'level': 'DEBUG', 'handlers': ['console']},
        'py.warnings': {'handlers': ['console']},
        '__force_dict__': True
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        }
    },
    'formatters': {
        'simple': {
            'format': ('%(asctime)s %(levelname)-5.5s [%(name)s]'
                       '[%(threadName)s] %(message)s')
        }
    }
}

# Custom Configurations must be in Python dictionary format::
#
# foo = {'bar':'baz'}
#
# All configurations are accessible at::
# pecan.conf
