'''
This test class defines unit tests for the csweb public views.

Created on Jan 25, 2014

@author: kvlinden
'''
from datetime import datetime

from test.base import CSWebTestBase


class CSWebTestViews(CSWebTestBase):
 
    def test_index_redirect(self):
        self.assertRedirects(self.app.get('/index'), '/')
                
    def test_index(self):
        # Go to the home page and make sure that the image, title and news items from the test db are there.
        response = self.app.get('/')
        self.assertRegexpMatches(response.data, '.*image_0.jpg.*')  # There is only one appropriately tagged image.
        # The administration options should not be visible.
        #self.assertNotRegexpMatches(response.data, '.*admin.*') # This is defined but not shown.
        # Check that the two canned news items are there and are linked appropriately.
        self.assertRegexpMatches(response.data, '.*news_0.*')
        self.assertRegexpMatches(response.data, '.*news_1.*')
        # Footer should always display the current year.
        self.assertRegexpMatches(response.data, '.*' + datetime.now().strftime('%Y') + '.*')

    def test_about(self):
        # Go to the about page and make user that the title and content are there.
        response = self.app.get('/about')
        self.assertRegexpMatches(response.data, '.*cs long description.*')
               
    def test_contact(self):
        # Go to the contact page and make sure that the contact-us form is there. 
        response = self.app.get('/contact')
        self.assertRegexpMatches(response.data, '.*Contact Us.*')
        # Form footers should also display the current year.
        #self.assertRegexpMatches(response.data, '.*' + datetime.now().strftime('%Y') + '.*') # This must have been removed.

    def test_academics(self):
        # Go to the academics page and make sure that it presents a list of
        # programs and links to their pages.
        response = self.app.get('/academics')
        self.assertRegexpMatches(response.data, '.*Computer Science.*')
        self.assertRegexpMatches(response.data, '.*academics/bacs.*')
        self.assertRegexpMatches(response.data, '.*Information Systems.*')
        self.assertRegexpMatches(response.data, '.*academics/bais.*')
        self.assertRegexpMatches(response.data, '.*Digital Communication.*')
        self.assertRegexpMatches(response.data, '.*academics/badc.*')

#     def test_academics_programs(self):
#         # Go to the BCS program page and make sure that it presents a list of courses and links to their pages (on our site).
#         response = self.app.get('/academics/bcs')
#         self.assertRegexpMatches(response.data, '.*.BCS*')
#         self.assertRegexpMatches(response.data, '.*courses/cs/108.*')
#         # Go to the BACS program page and make sure that it presents a list of courses and links to their pages (on our site).
#         response = self.app.get('/academics/bacs')
#         self.assertRegexpMatches(response.data, '.*.BACS*')
#         self.assertRegexpMatches(response.data, '.*courses/cs/112.*')
#         # Go to the BAIS program page and make sure that it presents a list of courses and links to their pages (on our site).
#         response = self.app.get('/academics/bais')
#         self.assertRegexpMatches(response.data, '.*Information Systems.*')
#         self.assertRegexpMatches(response.data, '.*courses/is/271.*')
#         # Go to the BADC program page and make sure that it presents a list of courses and links to their pages (on our site).
#         response = self.app.get('/academics/badc')
#         self.assertRegexpMatches(response.data, '.*Digital Communication.*')
#         self.assertRegexpMatches(response.data, '.*courses/cs/100.*')

    def test_news(self):
        # Go to the news page and make sure the two news items are there with only the teaser content.
        response = self.app.get('/news')
        self.assertRegexpMatches(response.data, '.*news_1 title.*')
        self.assertRegexpMatches(response.data, '.*news_1 teaser.*')
        self.assertRegexpMatches(response.data, '.*news_0 title.*')
        self.assertRegexpMatches(response.data, '.*news_0 teaser.*')

    def test_news_item(self):
        # Test a news item page.
        response = self.app.get('/news/news_0')
        self.assertRegexpMatches(response.data, '.*news_0 title.*')
        self.assertRegexpMatches(response.data, '.*news_0 content.*')

    def test_faculty_list(self):
        # Check that faculty and staff are all there.
        response = self.app.get('/people')
        self.assertRegexpMatches(response.data, '.*Adams.*')
        self.assertRegexpMatches(response.data, '.*Geneva College.*')
        self.assertRegexpMatches(response.data, '.*Pruim.*')
        self.assertRegexpMatches(response.data, '.*Nyhoff.*')
#         self.assertRegexpMatches(response.data, '.*Draving.*')
#         self.assertRegexpMatches(response.data, '.*System Administrator.*')

    def test_images(self):
        # Ensure that the main page has the only image tagged for 'department.cs'.
        response = self.app.get('/')
        self.assertRegexpMatches(response.data, '.*image_0.*')

    def test_documents(self):
        # Ensure that the test document is there.
        response = self.app.get('/documents/document1')
        self.assertRegexpMatches(response.data, '.*document1 title.*')
        self.assertRegexpMatches(response.data, '.*document1 content.*')

    def test_scholarships(self):
        # Ensure that the test scholarship is there.
        response = self.app.get('/scholarships/scholarship1')
        self.assertRegexpMatches(response.data, '.*scholarship1 title.*')

    def test_missing_pages(self):
        # Make sure that non-existent pages generate missing-resource errors.
        # Note that the app isn't designed to serve up real images, e.g., /images/image_0.
        for url in ['/blob', '/academics/blob', 'admin/blob', '/blob/blob']:
            response = self.app.get(url)
            self.assert404(response)

    def test_non_admin(self):
        # Make sure that only administrators are able to access these pages.
        self.assertRedirects(self.app.get('/admin'), '/login?next=http%3A%2F%2Flocalhost%2Fadmin')
        self.assertRedirects(self.app.get('/admin/images'), '/login?next=http%3A%2F%2Flocalhost%2Fadmin%2Fimages')

