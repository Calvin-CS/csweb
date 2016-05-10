'''
This module loads the unit tests for csweb application so that they can be
run as a Python test in PyCharm or, to see some error output that is not
displayed by PUnit, run on the Linux command line using:

   venv/bin/python -m unittest run_test

Each test uses a separate (but equal) database. MongoDB must be running.

NB. If using Eclipse/PyDev, Eclipse will discontinue console output if you uncheck
Eclipse-'Run Configurations'-common-'Allocate Console', but this turns off
the console output that can help debug runtime errors that mess up the
testing.

Created on Jan 22, 2014

@author: kvlinden
'''

# To run using PyDev-PyUnit, just hard-code the test classes here.
from test.views import *
from test.authentication import *
from test.mail import *
from test.base import *


# Here, the test class modules are hard-coded. The following code can be used
# to dynamically load tests in the given test package/folder, but it must be
# run as a Python app and cannot, thus, present its output in PyDev's PyUnit
# view.
#
#     config = TestingConfig()
#     testsuite = unittest.TestLoader().discover(config.TEST_DIR)
#     unittest.TextTestRunner(verbosity=config.TEST_VERBOSITY).run(testsuite)
#
