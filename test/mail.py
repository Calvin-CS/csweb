'''
This test class defines unit tests for the csweb contact-us emails.

Created on July 16, 2014

@author: kvlinden
'''
from app.units.contacts import Contacts
from test.base import CSWebTestBase, mail


class CSWebTestMail(CSWebTestBase):
 
    def test_contact_mail(self):
        # Make sure that the contact object can send emails.
        contactForm = Contacts()
        contactForm.subject.data = 'test subject'
        with mail.record_messages() as outbox:
            Contacts.send_email(mail, contactForm)
            assert len(outbox) == 1
            assert outbox[0].subject == 'test subject'
            assert outbox[0].recipients[0] == 'test@test.com'  # This values is set in TestingConfig.
            
# We'd need to stub out the call to Contacts.send_email() to make this work.
#     def test_contact_view(self):
#         # Make sure that users can send emails using contact-us.
#         self.contact('test subject', 'test@test.com')

            
    # Utility functions...
    
#     def contact(self, subject, email, follow_redirects=True):
#         return self.app.post('/contact', data={'subject' : subject, 'email' : email, 'submit' : 'Login'}, follow_redirects=follow_redirects)

    

                
