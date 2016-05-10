'''
This test class defines unit tests for the csweb administrative views and authentication.

Created on Jan 25, 2014

@author: kvlinden
'''
from flask.globals import g

from app.units.documents import Documents
from app.units.images import Images
from test.base import CSWebTestBase


class CSWebTestAuthentication(CSWebTestBase):
 
    def test_login_failure(self):
        # Make sure that logins with an unknown username or a bad password get sent back to /login with an error message.
        response = self.login('blob', 'password') 
        self.assertRegexpMatches(response.data, '.*Login*')
        self.assertRegexpMatches(response.data, '.*invalid login*')
        response = self.login('user', 'blob') 
        self.assertRegexpMatches(response.data, '.*Login*')
        self.assertRegexpMatches(response.data, '.*invalid login*')
 
    def test_cancel(self):
        # Make sure that administrators can cancel their login and return to the main page.
        response = self.cancel()
        self.assertGoesHome(response)
 
    def test_login(self):
        # Make sure that administrators can login, access the administration pages and see the edit/logout options.
        response = self.login('user', 'password')
        self.assertGoesAdmin(response)
        # Make sure that the admin page makes Administration current but not News.
        response = self.app.get('/admin')
        self.assertGoesAdmin(response)
        # Make sure the sub-admin pages list the db elements of the appropriate type.
        response = self.app.get('/admin/images')
        self.assertRegexpMatches(response.data, '.*image_0.*')
        self.assertRegexpMatches(response.data, '.*image_1.*')
        # Make sure that the admin options are available on other pages and that they have the appropriate links.
        response = self.app.get('/about')
        self.assertRegexpMatches(response.data, '.*/logout.*')

    def test_logout(self):
        # Administrators who logout are redirected to the main page, are shown no admin options and can no longer access the admin features.
        self.login('user', 'password') 
        response = self.logout()
        self.assertGoesHome(response)
        #self.assertNotRegexpMatches(response.data, '.*/logout.*')  #This menu is still defined in HTML but is not being shown.
        self.assertRedirects(self.app.get('/admin'), 
                             '/login?next=http%3A%2F%2Flocalhost%2Fadmin')

    def test_image_admin(self):
        # Make sure that the app allows administrators to create, edit and delete images.
        # Note that the create tool doesn't upload raw images; the administrator is assumed to have done that already.
        # Login first.
        self.login('user', 'password') 
        # Start by making sure that test_image doesn't exist in the admin list of images.
        response = self.app.get('/admin/images')
        self.assertNotRegexpMatches(response.data, '.*test_image.*')
        # Create a new test_image.
        response = self.app.post('/images/create',
                                 data={'submit' : 'Create',  # This is the form action button.
                                       'nameField': 'test_image_name',
                                       'filenameField' : 'test_image.jpg',
                                       'descriptionField' : 'test_image description',
                                       'tagsField' : '[u\'test_tag\']'},
                                 follow_redirects=True)
        # Make sure that test_image now exists with the correct content
        self.assertRegexpMatches(response.data, '.*test_image.*')
        # Edit the new test_image, it should be named "image_0" because of the starting state of the counters in the test database.
        mongoId = str(Images.read_unit('test_image_name').get('_id'))
        response = self.app.post('/images/test_image_name/edit',
                                 data={'submit' : 'Update',
                                       'idField': mongoId,
                                       'nameField' : 'test_image_name',
                                       'filenameField' : 'test_image_edited.jpg',
                                       'descriptionField' : 'test_image description edited',
                                       'tagsField' : '[u\'test_tag\', \'new_tag\']'},
                                 follow_redirects=True)
        # Make sure that the edited test_image now exists with the modified content
        self.assertRegexpMatches(response.data, '.*test_image_edited.*')
#         self.assertRegexpMatches(response.data, '.*test_image description edited.*')
        # Delete the new test_image.
        response = self.app.get('/images/test_image_name/delete')
        # Make sure that test_image doesn't exist anymore.
        response = self.app.get('/admin/images')
        self.assertNotRegexpMatches(response.data, '.*test_image.*')

    def test_document_admin(self):
        # Make sure that the app allows administrators to create, edit and delete documents.
        # Login first.
        self.login('user', 'password') 
        # Start by making sure that test_document doesn't exist in the admin list of documents.
        response = self.app.get('/admin/documents')
        self.assertNotRegexpMatches(response.data, '.*test_document.*')
        # Create a new test_document.
        response = self.app.post('/documents/create',
                                 data={'submit' : 'Create',  # This is the form action button.
                                       'nameField' : 'test_document_name',
                                       'titleField' : 'test_document title',
                                       'contentField' : 'test_document content'},
                                 follow_redirects=True)
        # Make sure that test_document now exists with the correct content
        self.assertRegexpMatches(response.data, '.*test_document.*')
        # Edit the new test_document as created above; get the mongoId first.
        mongoId = str(Documents.read_unit('test_document_name').get('_id'))
        response = self.app.post('/documents/test_document_name/edit',
                                 data={'submit': 'Update',
                                       'idField': mongoId,
                                       'nameField': 'test_document_name',
                                       'titleField': 'test_document title edited',
                                       'contentField': 'test_document content edited'},
                                 follow_redirects=True)
        # Make sure that the edited test_document now exists with the modified content
        self.assertRegexpMatches(response.data, '.*test_document title edited.*')
        self.assertRegexpMatches(response.data, '.*test_document content edited.*')
        # Delete the new test_document.
        response = self.app.get('/documents/test_document_name/delete')
        # Make sure that test_document doesn't exist anymore.
        response = self.app.get('/admin/documents')
        self.assertNotRegexpMatches(response.data, '.*test_document.*')

    def test_technews_admin(self):
        # Make sure that the app allows administrators to run the filter.
        # Login first.
        self.login('user', 'password')
        # Start by making sure that a list of articles is produced.
        response = self.app.get('/admin/technews')
        self.assertRegexpMatches(response.data, '.*technews.*')

    def test_technews_admin_refresh(self):
        # Make sure that the app allows administrators to refresh the filter.
        # Login first.
        self.login('user', 'password')
        # The refresh should also return a list of articles.
        response = self.app.get('/admin/technews/refresh')
        self.assertRegexpMatches(response.data, '.*technews.*')
        # Now, check that the main page lists technews articles.
        response = self.app.get('/')
        self.assertRegexpMatches(response.data, '.*Tech News.*')

    # Utility Functions
    def login(self, name, password, follow_redirects=True):
        return self.app.post('/login', data={'nameField' : name, 'passwordField' : password, 'submit' : 'Login'}, follow_redirects=follow_redirects)
 
    def cancel(self, follow_redirects=True):
        return self.app.post('/login', data={'cancel' : 'Cancel'}, follow_redirects=follow_redirects)
 
    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def assertGoesHome(self, response):
        '''Checks that the response is the homepage. 
        The homepage is assumed to not have breadcrumbs.'''
        return self.assertNotRegexpMatches(response.data, '.*crumb.*')
 
    def assertGoesAdmin(self, response):
        '''Checks that the response is the admin page. 
        The admin page is assumed to be titled "admin" and to have a logout option.'''
        return self.assertRegexpMatches(response.data, '.*Admin.*')    
