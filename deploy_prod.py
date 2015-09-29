'''
This module remote-copies the csweb files to a remote server, runs the unit
tests and restarts the wWSGI service. The root password must be entered.
It does not modify the production database; that must be modified on the
server, either by hand or using the CMS tools built into the system.

This module assumes that Linux/Nginx/uWSGI/Mongo are already running.

See ../readme.txt for installation and configuration notes.

Created on Feb 4, 2014

@author: kvlinden
'''

import os

print os.system('"C:\Program Files (x86)\WinSCP\WinSCP.com" /script=utils/deploy.txt')
