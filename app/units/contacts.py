'''
This module defines the features required to support the contact-us form. See
unitForm.py for more details. It doesn't not provide any information access
and, thus, does not inherit from unit.py.

The contact information for the department(s) is stored in the department
information unit. This form is separate because it is different from the
department information update form.

Created on Jul 15, 2014

@author: kvlinden
'''
from flask.globals import current_app
from wtforms import validators
from wtforms.fields.simple import TextField, TextAreaField

from app.units.unitForm import UnitForm
from flask.ext.mail import Message  # @UnresolvedImport


class Contacts(UnitForm):
    '''This class encapsulates tools for collecting contact information.
    These are not information units.
    '''

    @classmethod
    def send_email(cls, mail, form):
        '''Send the content of the given form to the default email address.'''
        subject = form.subject.data or 'empty'
        email = form.email.data or 'anonymous@anonymous.org'
        name = form.nameField.data or 'anonymous'
        message = form.message.data or 'empty'
        msg = Message(subject,
                      sender=email,
                      recipients=[current_app.config['MAIL_USERNAME']],
                      cc=[email])
        msg.body = '   From: %s\n  Email: <%s>\nMessage: %s' % \
            (name, email, message)
        with mail.connect() as conn:
            conn.send(msg)

    nameField = TextField("Name",
                          [validators.Required("Please enter your name.")])
    email = TextField("Email",
                      [validators.Required("Please enter your email address."),
                       validators.Email("Please enter your email address.")])
    subject = TextField("Subject",
                        [validators.Required("Please enter a subject.")])
    message = TextAreaField("Message",
                            [validators.Required("Please enter a message.")])
