'''
This module establishes the web resources for the application. These resources
map from the domain information units in the database to the rhetorical
structure of the web output.

Given the unified template structure provided by templates/content.html, this
module must construct some content and formatting to fill the slots provided
by the template. These formatting tasks are generally supported by methods
in utilties.py.

The main page is at /.

Created on Dec 30, 2013

@author: kvlinden
@author: dad32
'''
from functools import wraps

from flask import request, redirect, url_for
from flask.blueprints import Blueprint
from flask.globals import session
from flask.helpers import flash
from passlib.apps import custom_app_context

from app import mail
from app.units.contacts import Contacts
from app.units.courses import Courses
from app.units.departments import Departments
from app.units.documents import Documents
from app.units.images import Images
from app.units.news import News
from app.units.people import People
from app.units.programs import Programs
from app.units.resources import Resources
from app.units.scholarships import Scholarships
from app.units.tech_news import TechNews
from app.units.users import Users
from app.utilities import check_unit, display_content, \
    create_brief_news_list, get_breadcrumbs, \
    create_admin_list, create_hyperlink, create_image_list, \
    create_programs_list, create_people_list, \
    create_full_news_list, get_name, create_document_list, \
    create_program_tab_list, is_safe_url, is_logged_in, is_admin_page, \
    ERROR_404_MESSAGE, create_admin_resources_list, create_resources_list, \
    create_scholarships_list, create_admin_scholarships_list, create_resource_tab_list, \
    create_scholarship_content, create_scholarship_side,\
    create_admin_programs_list, create_newsarticle_list, create_techNewsarticle_list, create_course_tab_list


# Create a blueprint for the web-based views provided by the system.
# Blueprints were not strictly necessary for this simple application but they
# supported the creation of the application factory.
web = Blueprint('web', __name__,
                template_folder='templates',
                static_folder='static')


# -----------------------------------------------------------------------------
# Authentication route handlers...

def login_required(f):
    '''This utility decorator is used to mark route methods as
    administrator-only methods. It records the original destination so that the
    user/administrator can be redirected there after a successful login. Set it
    as the last decorator, immediately before the method definition.
    '''
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_logged_in():
            return redirect(url_for('web.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@web.route('/login', methods=['GET', 'POST'])
def login():
    '''This routine verifies that the user is an administrator and, if so,
    puts them in admin mode and redirects them to the admin resource they
    originally requested. It sends them back to the main page if their
    requested URL is unsafe. The username and password are stored in
    the database.
    '''
    if is_logged_in():
        return redirect(url_for('web.display_admin'))
    target_url = request.values.get('next') or url_for('web.display_admin')
    if not is_safe_url(target_url):
        return redirect(url_for('web.display_index'))
    form = Users()
    if form.is_submitted():
        # Check if the cancel button has been pressed; the form value will be
        # 'Cancel' but this doesn't need to be checked.
        if request.form.get('cancel'):
            return redirect(url_for('web.display_index'))
        if form.validate():
            user = Users.read_unit(form.nameField.data)
            if (user is not None) and \
                   (custom_app_context.verify(form.passwordField.data,
                                          user['password'])):
                session['logged_in'] = True
                return redirect(target_url)
        flash('invalid login...', 'error')
    return display_content(
        form=form,
        next=target_url,
        title='Login',
        breadcrumbs=get_breadcrumbs('login')
    )


@web.route('/logout')
def logout():
    '''This routine logs the user out. If they were on a administrator page
    it returns them to the main site index file. If they were on an
    unrestricted page, it returns them to the page they were on.
    '''
    session.pop('logged_in', None)
    target_url = request.values.get('next')
    if target_url is not None and \
            not is_admin_page(target_url) and \
            is_safe_url(target_url):
        return redirect(target_url)
    return redirect(url_for('web.display_index'))


# -----------------------------------------------------------------------------
# Department information route handlers...


@web.route('/')
@web.route('/index', alias=True)
def display_index():
    '''Configure and display the main index page, with an appropriate image,
    the department short description and a list of current news articles.
    '''
    department = check_unit(Departments.read_unit('cs'))
    return display_content(
        image=Images.read_tagged_unit('departments.cs'),
        title=department.get('title'),
        subtitle=department.get('tagline'),
        primary=department.get('shortDescription'),
        sideTitle='Computing News',
        sideList=create_brief_news_list(News.read_units(limit=2 + TechNews.TECH_NEWS_LIMIT)),
        editable=True,
        editableUrl=url_for('web.update_department', name='cs')
    )


@web.route('/about')
def display_about():
    '''Configure and display the about page, with an appropriate image and the
    department long description.
    '''
    department = check_unit(Departments.read_unit('cs'))
    return display_content(
        breadcrumbs=get_breadcrumbs('about'),
        image=Images.read_tagged_unit('about'),
        title='About Us',
        primary=department.get('longDescription'),
        editable=True,
        editableUrl=url_for('web.update_department', name='cs')
    )


@web.route('/departments/<name>/edit', methods=['GET', 'POST'])
@login_required
def update_department(name):
    '''Configure the editing for the about page, which must edit the long
    description of the department. There is only one department, name==cs.

    For GET requests, this method allows the administrator to edit the named
    document. For POST requests, this method saves the edits made by the
    administrator and then reloads/redisplays the document administration page.
    Non-authenticated users are redirected to the login page. documents that
    don't exist can't be edited. Because we don't show individual documents,
    all redirects go to the documents administration page.
    '''
    form = Departments()
    if form.is_submitted():
        if form.validate() and request.form.get('submit'):
            Departments.update_unit(form)
    else:
        department = Departments.read_unit(name)
        if department:
            form.initialize(name=name, action='update', department=department)
            return display_content(
                form=form,
                title='Edit: ' + name,
                breadcrumbs=get_breadcrumbs('departments', name, 'edit')
            )
    return redirect(url_for('web.display_about'))


# -----------------------------------------------------------------------------
# Administration route handlers...

@web.route('/admin')
@login_required
def display_admin():
    '''This routine displays the site administration page.'''
    return display_content(
        breadcrumbs=get_breadcrumbs('admin'),
        title='Administration',
        primary='''<p>
                   The program, course, faculty and news resources
                   used on this site are administered by CIT; change
                   them by emailing helpdesk. These other resources are
                   managed by the department content management system;
                   you can do the following things with them yourself.
                   </p>
                   ''',
        primaryList=create_admin_list(),
        primaryListHr=False,
        editable=False
    )


@web.route('/admin/images')
@web.route('/images', alias=True)
@web.route('/images/', alias=True)
@login_required
def display_admin_images():
    '''This routine displays the administration tools for images. It maps both
    web routes to support certain unused breadcrumb trails.
    '''
    return display_content(
        breadcrumbs=get_breadcrumbs('admin', 'images'),
        title='Administration: Images',
        primary=create_hyperlink(url_for('web.create_image'),
                                 'Create a new image'),
        primaryList=create_image_list(Images.read_units()),
        primaryListHr=True,
        editable=False
    )


@web.route('/admin/documents')
@web.route('/documents', alias=True)
@web.route('/documents/', alias=True)
@login_required
def display_admin_documents():
    '''This routine displays the administration tools for user documents. It is
    password protected because the listing page allows administrative features.
    Documents should be accessed as linked from existing pages.
    '''
    return display_content(
        breadcrumbs=get_breadcrumbs('admin', 'documents'),
        title='Administration: Documents',
        primary=create_hyperlink(url_for('web.create_document'),
                                 'Create a new document'),
        primaryList=create_document_list(Documents.read_units()),
        primaryListHr=True,
        editable=False
    )


@web.route('/admin/scholarships')
@login_required
def display_admin_scholarships():
    '''This routine displays the administration tools for user documents. It is
    password protected because the listing page allows administrative features.
    Documents should be accessed as linked from existing pages.
    '''
    scholarships = Scholarships.read_units()
    return display_content(
        breadcrumbs=get_breadcrumbs('admin', 'scholarships'),
        title='Administration: Scholarships',
        primary=create_hyperlink(url_for('web.create_scholarship'),
                                 '''Create a new scholarship
                                    (in the CS database only)'''),
        primaryList=create_admin_scholarships_list(scholarships),
        primaryListHr=True,
        editable=True
    )


@web.route('/admin/resources')
@login_required
def display_admin_resources():
    '''This routine displays the administration tools for resource units. It is
    password protected because the listing page allows administrative features.
    '''
    return display_content(
        breadcrumbs=get_breadcrumbs('admin', 'resources'),
        title='Administration: Resources',
        primaryList=create_admin_resources_list(Resources.read_units()),
        primaryListHr=True,
        editable=False
    )


@web.route('/admin/programs')
@login_required
def display_admin_programs():
    '''This routine displays the administration tools for program units. It is
    password protected because the listing page allows administrative features.
    Only the model schedules can be edited; the rest of the data comes from
    CIT.
    '''
    return display_content(
        breadcrumbs=get_breadcrumbs('admin', 'programs'),
        title='Administration: Programs',
        primaryList=create_admin_programs_list(Programs.read_units()),
        primaryListHr=True,
        editable=False
    )


@web.route('/admin/news')
@login_required
def display_admin_news():
    '''This routine displays the administration tools for news.
    We'll eventually use CIT's news tools.
    '''
    return display_content(
        breadcrumbs=get_breadcrumbs('admin', 'news'),
        title='Administration: News Articles',
        primary=create_hyperlink(url_for('web.create_news_article'),
                                 'Create a news article'),
        primaryList=create_newsarticle_list(News.read_units()),
        primaryListHr=True,
        editable=False
    )


@web.route('/admin/technews')
@login_required
def display_admin_tech_news():
    '''This routine displays the administration tools for tech news from feeds.
    '''
    return display_content(
        breadcrumbs=get_breadcrumbs('admin', 'technews'),
        title='Administration: TechNews Articles',
        primary='<p>Thumbs up/down relevant news articles to adjust the list of articles. ' +
        '<a href = "/admin/technews/refresh" >Click here to refresh the page listings.</a></p>' +
        '<p>To see the current items <a href="/admin/news">click here.</a></p>',
        primaryList=create_techNewsarticle_list(TechNews.read_units(refreshList = False)),
        primaryListHr=True,
        editable=False
    )


@web.route('/admin/technews/refresh')
@login_required
def display_refresh_admin_tech_news():
    '''This routine displays the administration tools for tech news from feeds
        It also refreshes the home page content.
    '''
    return display_content(
        breadcrumbs=get_breadcrumbs('admin', 'technews'),
        title='Administration: TechNews Articles',
        primary='<p>Thumbs up/down relevant news articles to adjust the list of articles. ' +
        '<a href = "/admin/technews/refresh" >Click here to refresh the page listings.</a></p>' +
        '<p>To see the current items <a href="/admin/news">click here.</a></p>',
        primaryList=create_techNewsarticle_list(TechNews.read_units(refreshList=True, unitsDisplay=TechNews.TECH_NEWS_LIMIT)),
        primaryListHr=True,
        editable=False
    )

# -----------------------------------------------------------------------------
# The contact us handler...

@web.route('/contact', methods=['GET', 'POST'])
def contact():
    '''Configure and display the contact us page, with its input form and
    email feature.
    '''
    form = Contacts()
    if form.is_submitted():
        if request.form.get('cancel'):
            return redirect(url_for('web.display_index'))
        if form.validate():
            Contacts.send_email(mail, form)
            return redirect(url_for('web.display_index'))
        flash('All fields are required.')
    department = Departments.read_unit('cs')
    return display_content(
        form=form,
        title='Contact Us',
        primary=department.get('contact'),
        sideTitle='Admissions at Calvin',
        sideContent='''<p>Interested in what Calvin has to offer?<br>
    <a href="http://www.calvin.edu/admissions/visit/">Schedule a visit</a>
    or <br><a href="http://www.calvin.edu/admissions/contact/request/">request
    more information</a>.</p>''',
        breadcrumbs=get_breadcrumbs('contact'),
        editable=True,
        editableUrl=url_for('web.update_department', name='cs')
    )


# -----------------------------------------------------------------------------
# Academics information route handlers...

@web.route('/academics')
@web.route('/programs', alias='True')
def display_programs():
    '''Configure and display the academics overview page.'''
    return display_content(
        breadcrumbs=get_breadcrumbs('academics'),
        image=Images.read_tagged_unit('about'),
        title='Academics',
        primary='''The Department of Computer Science offers the following
                   academic programs. To learn more about our academics goals,
                   see our <a href="/administration/assessment/plan">program
                   outcomes</a>.''',
        primaryList=create_programs_list(Programs.read_units()),
        primaryListHr=False,
        editable=False
    )


@web.route('/academics/<name>')
def display_program(name=None):
    '''Configure and display a program page.'''
    program = check_unit(Programs.read_unit(name))
    return display_content(
        breadcrumbs=get_breadcrumbs('academics', program.get('name')),
        image=Images.read_tagged_unit(name),
        title=program.get('title'),
        primary=program.get('majorDescription'),
        tabList=create_program_tab_list(program),
        editable=True,
        editableUrl=url_for('web.update_program', name=name)
    )


@web.route('/academics/<name>/edit', methods=['GET', 'POST'])
@login_required
def update_program(name):
    '''Configure the editing for the program pages. Because all of the program
    data except the model schedule comes from CIT, this routine will only
    support updates to the model schedule. The administrator cannot edit
    the name of the program.
    '''
    form = Programs()
    if form.is_submitted():
        if form.validate() and request.form.get('submit'):
            Programs.update_unit(form)
    else:
        program = Programs.read_unit(name)
        if program:
            form.initialize(name=name, action='update', document=program)
            return display_content(
                form=form,
                title='Edit: ' + name,
                breadcrumbs=get_breadcrumbs('academics', name, 'edit')
            )
    return redirect(url_for('web.display_program', name=name))


@web.route('/academics/honors')
def display_honors():
    '''Display information on the honors program.'''
    department = check_unit(Departments.read_unit('cs'))
    return display_content(
        breadcrumbs=get_breadcrumbs('academics', 'honors'),
        image=Images.read_tagged_unit('academics.honors'),
        title='Graduating with Honors',
        primary=department.get('honors'),
        editable=True,
        editableUrl=url_for('web.update_department', name='cs')
    )


@web.route('/academics/courses')
@web.route('/courses', alias=True)
@web.route('/courses/', alias=True)
def display_courses():
    '''Configure and display the courses list page.'''
    department = check_unit(Departments.read_unit('cs'))
    courses = check_unit(Courses.read_units())
    return display_content(
        breadcrumbs=get_breadcrumbs('academics', 'courses'),
        image=Images.read_tagged_unit('courses'),
        title='Courses &amp; Materials',
        tabList=create_course_tab_list(courses, department),
        editable=True,
        editableUrl=url_for('web.update_department', name='cs')
    )


# -----------------------------------------------------------------------------
# Research information route handlers...

@web.route('/research')
def display_research():
    '''Configure and display the research overview page.'''
    department = check_unit(Departments.read_unit('cs'))
    return display_content(
        breadcrumbs=get_breadcrumbs('research'),
        image=Images.read_tagged_unit('research'),
        title='Research',
        primary=department.get('research'),
        editable=True,
        editableUrl=url_for('web.update_department', name='cs')
    )


# -----------------------------------------------------------------------------
# Faculty/Staff information route handlers...

@web.route('/people')
def display_people():
    '''Configure and display a list of faculty members.'''
    return display_content(
        breadcrumbs=get_breadcrumbs('people'),
        image=Images.read_tagged_unit('people'),
        title='Faculty and Staff',
        primaryList=create_people_list(People.read_units()),
        primaryListHr=True,
        editable=False
    )

# The current site links directly from the faculty list to the personal page of
# the faculty, with no separate, institutional faculty page.
# @web.route('/faculty/<name>')
# def display_faculty(name):
#     '''This routine displays a single faculty member.'''
#     facultyMember = get_faculty_person(name)
#     if facultyMember is None:
#         abort(404)
#     kwargs = {'title' : facultyMember[0].fullName,
#               'breadcrumbs' : get_breadcrumbs('faculty',
#                                               facultyMember[0].fullName)}
#     return display_resource_template('content_faculty_member.html',
#                                      faculty=facultyMember, **kwargs)


# -----------------------------------------------------------------------------
# News article route handlers...

@web.route('/news')
@web.route('/resources/news', alias=True)
def display_news():
    '''This routine displays the main news list page.'''
    return display_content(
        breadcrumbs=get_breadcrumbs('news'),
        title='Computing News',
        primaryList=create_full_news_list(News.read_units()),
        primaryListHr=True,
        editable=True,
        editableUrl=url_for('web.display_admin_news')
    )


@web.route('/news/<name>')
def display_news_article(name):
    '''This routine displays a single news article.'''
    article = check_unit(News.read_unit(name))
    return display_content(
        breadcrumbs=get_breadcrumbs('news', name),
        title=article.get('title'),
        subtitle=article.get('date').strftime('%B %d, %Y'),
        primary='<p>' + article.get('content') + '</p>',
        current=get_name('news', name),
        editable=True,
        editableUrl=url_for('web.update_news_article', name=name)
    )


@web.route('/news/<name>/edit', methods=['GET', 'POST'])
@login_required
def update_news_article(name):
    '''This routine does one of two things: if the user has asked to edit a
    news article (GET), it displays an editing form for the given article
    id, populated with the current database content; if the user has filled
    and submitted the editing form (POST), it writes the (modified) form
    contents into the database entry for the given article id.
    '''
    form = News()
    if form.is_submitted():
        if form.validate() and request.form.get('submit'):
            News.update_unit(form)
            return redirect(url_for('web.display_news_article', name=name))
    else:
        article = News.read_unit(name)
        if article:
            form.initialize(action='edit', unit=article)
            return display_content(
                form=form,
                title='Edit: ' + name,
                breadcrumbs=get_breadcrumbs('news', name, 'edit')
            )
    return redirect(url_for('web.display_admin_news'))


@web.route('/news/create', methods=['GET', 'POST'])
@login_required
def create_news_article():
    '''This routine does one of two things: if the user has asked to create a
    news article (GET), it displays an empty form for the user to use to
    create the new article; if the user has filled and submitted the creation
    form (POST), it writes the (new) form contents into the database entry
    under a new, unique id.
    '''
    form = News()
    if form.is_submitted():
        if form.validate() and request.form.get('submit'):
            name = News.create_unit(form)
            return redirect(url_for('web.display_news_article', name=name))
        else:
            return redirect(url_for('web.display_admin_news'))
    else:
        form.initialize(action='create')
        return display_content(
            form=form,
            title='Create Article',
            breadcrumbs=get_breadcrumbs('news', 'create')
        )


@web.route('/news/<name>/delete')
@login_required
def delete_news_article(name):
    '''This routine deletes the given news article. This is not restful;
    the system should accept only DELETE requests on /news/<name>.
    '''
    News.delete_unit(name)
    return redirect(url_for('web.display_admin_news'))




# -----------------------------------------------------------------------------
# TechNews article route handlers...
#The follwoing 2 functions are called by a javascript function that calls them when the up/down buttons are pressed in the adminstration pages..
@web.route('/admin/technews/<url>/up', methods=['GET', 'POST'])
@login_required
def up_technews_article(url):
    '''This routine does one of two things: if the user has asked to edit a
    news article (GET), it displays an editing form for the given article
    id, populated with the current database content; if the user has filled
    and submitted the editing form (POST), it writes the (modified) form
    contents into the database entry for the given article id.
    '''
        
    TechNews.up_unit(url)
    return redirect('#')

@web.route('/admin/technews/<url>/down', methods=['GET', 'POST'])
@login_required
def down_tech_news_article(url):
    '''This routine does one of two things: if the user has asked to edit a
    news article (GET), it displays an editing form for the given article
    id, populated with the current database content; if the user has filled
    and submitted the editing form (POST), it writes the (modified) form
    contents into the database entry for the given article id.
    '''
    TechNews.down_unit(url)
    return redirect('#')



@web.route('/admin/technews/<url>/up/refresh', methods=['GET', 'POST'])
@login_required
def up_technews_article_refresh(url, inNews= True):
    '''This routine does one of two things: if the user has asked to edit a
    news article (GET), it displays an editing form for the given article
    id, populated with the current database content; if the user has filled
    and submitted the editing form (POST), it writes the (modified) form
    contents into the database entry for the given article id.
    '''
        
    TechNews.up_unit(url, inNews= True)
    return redirect('/admin/technews/refresh')

@web.route('/admin/technews/<url>/down/refresh', methods=['GET', 'POST'])
@login_required
def down_tech_news_article_refresh(url,inNews= True):
    '''This routine does one of two things: if the user has asked to edit a
    news article (GET), it displays an editing form for the given article
    id, populated with the current database content; if the user has filled
    and submitted the editing form (POST), it writes the (modified) form
    contents into the database entry for the given article id.
    '''
    TechNews.down_unit(url,inNews= True)
    return redirect('/admin/technews/refresh')


# -----------------------------------------------------------------------------
# Image manipulation route handlers

@web.route('/images/<name>')
@login_required
def display_image(name):
    '''This routine displays a given image. We included only to support
    generally unused breadcrumb trails. It is password protected at the
    moment to ensure that users access raw images as part of actual pages.
    '''
    image = check_unit(Images.read_unit(name))
    return display_content(
        breadcrumbs=get_breadcrumbs('images', name),
        title=image.get('name'),
        primary='<img src="/static/images/' + image.get('filename') + '">',
        primaryListHr=False,
        editable=True,
        editableUrl=url_for('web.update_image', name=name)
    )


@web.route('/images/<name>/edit', methods=['GET', 'POST'])
@login_required
def update_image(name):
    '''For GET requests, this method allows the administrator to edit the named
       image. For POST requests, this method saves the edits made by the
       administrator and then reloads/redisplays the image admin page.
       Non-authenticated users are redirected to the login page. Images that
       don't exist can't be edited. Because we don't show individual images,
       all redirects go to the images admin page.
    '''
    form = Images()
    if form.is_submitted():
        if form.validate() and request.form.get('submit'):
            Images.update_unit(form)
            return redirect(url_for('web.display_image',
                            name=form.getName()))
    else:
        image = Images.read_unit(name)
        if image:
            form.initialize(name=name, action='update', image=image)
            return display_content(
                form=form,
                title='Edit: ' + name,
                breadcrumbs=get_breadcrumbs('images', name, 'edit')
            )
    return redirect(url_for('web.display_admin_images'))


@web.route('/images/create', methods=['GET', 'POST'])
@login_required
def create_image():
    '''This routine displays an editing page for creating an image.'''
    form = Images()
    if form.is_submitted():
        if form.validate() and request.form.get('submit'):
            Images.create_unit(form)
            return redirect(url_for('web.display_image',
                            name=form.getName()))
        else:
            return redirect(url_for('web.display_admin_images'))
    else:
        form.initialize(action='create')
        return display_content(
            form=form,
            title='Create Image',
            breadcrumbs=get_breadcrumbs('images', 'create')
        )


@web.route('/images/<name>/delete')
@login_required
def delete_image(name):
    '''This routine deletes the given image entry, but it leaves the actual
    image in place.
    '''
    Images.delete_unit(name)
    return redirect(url_for('web.display_admin_images'))


# -----------------------------------------------------------------------------
# Scholarships manipulation route handlers

@web.route('/scholarships/')
@web.route('/resources/scholarships', alias=True)
def display_scholarships():
    '''This routine displays the administration tools for user documents. It is
    password protected because the listing page allows administrative features.
    Documents should be accessed as linked from existing pages.
    '''
    scholarships = Scholarships.read_units()
    return display_content(
        breadcrumbs=get_breadcrumbs('scholarships'),
        title='Scholarships &amp; Awards',
        primaryList=create_scholarships_list(scholarships),
        primaryListHr=False,
        editable=True,
        editableUrl=url_for('web.display_admin_scholarships')
    )


@web.route('/scholarships/<name>')
def display_scholarship(name):
    '''This routine displays a given scholarship.'''
    scholarship = check_unit(Scholarships.read_unit(name))
    # Add scholarship details in side bar if they exist.
    sideContent = create_scholarship_side(scholarship)
    sideTitle = None
    if sideContent:
        sideTitle = 'Details'
    return display_content(
        breadcrumbs=get_breadcrumbs('scholarships', name),
        title=scholarship.get('title'),
        primary=create_scholarship_content(scholarship),
        sideTitle=sideTitle,
        sideContent=sideContent,
        primaryListHr=False,
        editable=True,
        editableUrl=url_for('web.update_scholarship', name=name)
    )


@web.route('/scholarships/<name>/edit', methods=['GET', 'POST'])
@login_required
def update_scholarship(name):
    '''For GET requests, this method allows the administrator to edit the named
    document. For POST requests, this method saves the edits made by the
    administrator and then reloads/redisplays the document administration page.
    Non-authenticated users are redirected to the login page. documents that
    don't exist can't be edited. Because we don't show individual documents,
    all redirects go to the documents administration page.
    '''
    form = Scholarships()
    if form.is_submitted():
        if form.validate() and request.form.get('submit'):
            Scholarships.update_unit(form)
            return redirect(url_for('web.display_scholarship',
                            name=form.getName()))
    else:
        scholarship = Scholarships.read_unit(name)
        if scholarship:
            form.initialize(name=name, action='update',
                            scholarship=scholarship)
            return display_content(
                form=form,
                title='Edit: ' + name,
                breadcrumbs=get_breadcrumbs('scholarships', name, 'edit')
            )
    return redirect(url_for('web.display_admin_scholarships'))


@web.route('/scholarships/create', methods=['GET', 'POST'])
@login_required
def create_scholarship():
    '''This routine displays an editing page for creating an scholarship.'''
    form = Scholarships()
    if form.is_submitted():
        if form.validate() and request.form.get('submit'):
            Scholarships.create_unit(form)
            return redirect(url_for('web.display_scholarships',
                            name=form.getName()))
        else:
            return redirect(url_for('web.display_admin_scholarships'))
    else:
        form.initialize(action='create')
        return display_content(
            form=form,
            title='Create Scholarship',
            breadcrumbs=get_breadcrumbs('scholarship', 'create')
        )


@web.route('/scholarships/<name>/delete')
@login_required
def delete_scholarship(name):
    '''This routine deletes the given document entry, but it leaves the
    actual document in place.
    '''
    Scholarships.delete_unit(name)
    return redirect(url_for('web.display_admin_scholarships'))


# --------------------------------------------------------------------------------------
# Document manipulation route handlers

@web.route('/documents/<name>')
def display_document(name):
    '''This routine displays a given document. It is not password protected
    because all documents are visible to all visitors.
    '''
    document = check_unit(Documents.read_unit(name))
    return display_content(
        breadcrumbs=get_breadcrumbs('documents', name),
        title=document.get('title'),
        primary=document.get('content'),
        primaryListHr=False,
        editable=True,
        editableUrl=url_for('web.update_document', name=name)
    )


@web.route('/documents/<name>/edit', methods=['GET', 'POST'])
@login_required
def update_document(name):
    '''For GET requests, this method allows the administrator to edit the named
    document. For POST requests, this method saves the edits made by the
    administrator and then reloads/redisplays the document administration page.
    Non-authenticated users are redirected to the login page. documents that
    don't exist can't be edited. Because we don't show individual documents,
    all redirects go to the documents administration page.
    '''
    form = Documents()
    if form.is_submitted():
        if form.validate() and request.form.get('submit'):
            Documents.update_unit(form)
            return redirect(url_for('web.display_document',
                            name=form.getName()))
    else:
        document = Documents.read_unit(name)
        if document:
            form.initialize(name=name, action='update', document=document)
            return display_content(
                form=form,
                title='Edit: ' + name,
                breadcrumbs=get_breadcrumbs('documents', name, 'edit')
            )
    return redirect(url_for('web.display_admin_documents'))


@web.route('/documents/create', methods=['GET', 'POST'])
@login_required
def create_document():
    '''This routine displays an editing page for creating an document.'''
    form = Documents()
    if form.is_submitted():
        if form.validate() and request.form.get('submit'):
            Documents.create_unit(form)
            return redirect(url_for('web.display_document',
                            name=form.getName()))
        else:
            return redirect(url_for('web.display_admin_documents'))
    else:
        form.initialize(action='create')
        return display_content(
            form=form,
            title='Create document',
            breadcrumbs=get_breadcrumbs('documents', 'create')
        )


@web.route('/documents/<name>/delete')
@login_required
def delete_document(name):
    '''This routine deletes the given document entry, but it leaves the actual
    document in place.
    '''
    Documents.delete_unit(name)
    return redirect(url_for('web.display_admin_documents'))


# ----------------------------------------------------------------------------
# Resource manipulation route handlers

@web.route('/resources')
def display_resources():
    '''Configure and display the resources overview page.'''
    return display_content(
        breadcrumbs=get_breadcrumbs('resources'),
        image=Images.read_tagged_unit('resources'),
        title='Department Resources',
        primary='''The Department of Computer Science offers the following
                   resources.''',
        primaryList=create_resources_list(Resources.read_units()),
        primaryListHr=False,
        editable=False
    )


@web.route('/resources/<name>')
def display_resource(name):
    '''This routine displays a given resource. It is not password protected
    because all resources are visible to all visitors.
    '''
    resource = check_unit(Resources.read_unit(name))
    return display_content(
        breadcrumbs=get_breadcrumbs('resources', name),
        title=resource.get('title'),
        primary=resource.get('content'),
        tabList=create_resource_tab_list(resource),
        editable=True,
        editableUrl=url_for('web.update_resource', name=name)
    )


@web.route('/resources/<name>/edit', methods=['GET', 'POST'])
@login_required
def update_resource(name):
    '''For GET requests, this method allows the administrator to edit the named
    resource. For POST requests, this method saves the edits made by the
    administrator and then reloads/redisplays the resource administration page.
    Non-authenticated users are redirected to the login page. resources that
    don't exist can't be edited. Because we don't show individual resources,
    all redirects go to the resources administration page.
    '''
    form = Resources()
    if form.is_submitted():
        if form.validate() and request.form.get('submit'):
            Resources.update_unit(form)
            return redirect(url_for('web.display_resource',
                            name=form.getName()))
    else:
        resource = Resources.read_unit(name)
        if resource:
            form.initialize(name=name, action='update', resource=resource)
            return display_content(
                form=form,
                title='Edit: ' + name,
                breadcrumbs=get_breadcrumbs('resources', name, 'edit')
            )
    return redirect(url_for('web.display_admin_resources'))


@web.route('/resources/create', methods=['GET', 'POST'])
@login_required
def create_resource():
    '''This routine displays an editing page for creating an resource.'''
    form = Resources()
    if form.is_submitted():
        if form.validate() and request.form.get('submit'):
            Resources.create_unit(form)
            return redirect(url_for('web.display_resource',
                            name=form.getName()))
        else:
            return redirect(url_for('web.display_admin_resources'))
    else:
        form.initialize(action='create')
        return display_content(
            form=form,
            title='Create resource',
            breadcrumbs=get_breadcrumbs('resources', 'create')
        )


@web.route('/resources/<name>/delete')
@login_required
def delete_resource(name):
    '''This routine deletes the given resource entry, but it leaves the actual
    resource in place.
    '''
    Resources.delete_unit(name)
    return redirect(url_for('web.display_admin_resources'))


# -----------------------------------------------------------------------------
# Redirects for some strategic old URLs...


@web.route('/p/ComputingCareersMarket')
def redirect_careers_url():
    '''This method redirects the old but popular URL for the careers page.'''
    return redirect(url_for('web.display_document', name='computing_careers'))


# -----------------------------------------------------------------------------
# Error handlers...


@web.app_errorhandler(404)
def page_not_found(e):
    return display_content(
        title='''Page not found...''',
        primary=ERROR_404_MESSAGE,
        editable=False
    ), 404
