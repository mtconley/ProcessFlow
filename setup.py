try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

import sys

config = {
    'description': 'ProcessFlow is a simple wrapper for pygraphvis to make process flow diagrams',
    'author': 'Matthew Conley',
    'url': 'https://github.com/mtconley/ProcessFlow',
    'download_url': 'https://github.com/mtconley/ProcessFlow.git.',
    'author_email': '',
    'version': 0.0.1,
    'install_requires': 
        [
            'pygraphviz'
        ],
    'packages': find_packages(),
    'name': 'ProcessFlow'
}

print "system is: " + sys.platform
print ''
print "installing dependencies... "
print config['install_requires']

setup(**config)