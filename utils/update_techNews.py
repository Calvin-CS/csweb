#!/srv/www/calvin.edu/csweb/venv/bin/python

'''
This function updates the technews articles. by logging into the server and
calling the refresh page.

@author: David Dick, dad32
@version:2015.03.07

Replaced id/passwd with command-line arguments -kvlinden, 11may2016

'''

import sys

from twill.commands import go, fv, formaction, submit

# Uncomment the lines below for debugging purposes.
go('http://127.0.0.1/login')
#showforms()  
fv("1", "nameField", sys.argv[1])
fv("1", "password", sys.argv[2])
formaction('form','http://127.0.0.1/login')
submit("4")
#show()
go('http://127.0.0.1/admin/technews/refresh')
