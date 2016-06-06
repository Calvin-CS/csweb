'''
These functions implement utilities used by the view methods. They include
tools for creating rhetorical content from domain information from the
database and some basic utilities used throughout the system.

Created on Jan 22, 2014

@author: kvlinden
@author: dad32
'''

from datetime import datetime
import re
from urlparse import urlparse, urljoin

from flask import session, render_template
from flask.globals import g, request
from flask.helpers import url_for
from werkzeug import abort


def display_content(**kwargs):
    '''This routine displays a webpage for the given content, adding named
    values for administrative users, date/time and all fields provided by
    the calling program. The content.html template and its include files are
    assumed to be configured to handle these named values.

    If the kwargs include setting editable to true, a suitable ./edit route
    handler must be configured in views.py.
    '''
    return render_template(
        "content.html",
        admin=is_logged_in(),
        date_time=datetime.now(),
        **kwargs
    )


# -----------------------------------------------------------------------------
# Rhetorical content constructors...

def create_brief_news_list(newsList):
    return create_news_list(
        newsList,
        includeSummary=True,
        includeLink=True,
        includeOtherNewsLink=True
    )


def create_full_news_list(newsList):
    return create_news_list(
        newsList,
        includeTitle=True,
        includeDate=True,
        includeSummary=True,
        includeLink=True
    )


def create_news_list(newsList,
                     includeTitle=False,
                     includeDate=False,
                     includeSummary=False,
                     includeContent=False,
                     includeLink=False,
                     includeOtherNewsLink=False):
    '''This routine converts the domain content in the news article list into a
    list of rhetorical content, including the particular elements as specified.
    It produces a list of one dictionary because there is only one section in
    the news list. See the full description of this mechanism in
    content_list.html.
    '''
    newsItems = []
    techNews = []

    for newsItem in newsList:
        # This Separates the tech news articles from the rest of the news feed.

        if newsItem.get('name').startswith('tech_news'):
            entry = {}
            if includeTitle:
                entry['title'] = newsItem.get('title')
            # Include the summary, the full article, or both.
            content = ''
            if includeDate:
                content += '<em>' + format_date(newsItem.get('date')) + \
                    '</em><br><br>'
            if includeSummary:
                content += newsItem.get('title')
            if includeContent:
                content += newsItem.get('content')
            if includeLink:
                link = newsItem.get('summary')
                if link != None:
                    content += \
                        ' <small>' + \
                        '<a href= "' + link + '" target="_blank" class="external"> <em>read more...</em></a>' + \
                        '</small>'
            entry['subContent'] = content
            techNews.append(entry)
        else:
            entry = {}
            if includeTitle:
                entry['title'] = newsItem.get('title')
            # Include the summary, the full article, or both.
            content = ''
            if includeDate:
                content += '<em>' + format_date(newsItem.get('date')) + \
                    '</em><br><br>'
            if includeSummary:
                content += newsItem.get('summary')
            if includeContent:
                content += newsItem.get('content')
            if includeLink:
                link = '/news/' + newsItem.get('name')
                content += \
                    ' <small>' + \
                    create_hyperlink(link, '<em>read more...</em>') + \
                    '</small>'
            entry['subContent'] = content
            newsItems.append(entry)

    if includeOtherNewsLink:
        newsItems.append({'subContent': ' <small>' +
                          create_hyperlink('/news',
                                           '<em>see other department articles...</em>') +
                          '</small>'})
    if len(techNews) > 0 and includeOtherNewsLink:
        newsItems.append({'subContent': ' <h3>' +
                          'Recent Tech News' +
                          '</h3>'})
        for news in reversed(techNews):
            newsItems.append(news)
    result = []
    result.append({'title': 'Computing News', 'sectionItems': newsItems})
    return result


def create_programs_list(programsList):
    '''This routine converts the domain content in the programs list into a
    list of rhetorical elements described in includes/content_primary.html.
    It produces a list of one dictionary because there is only one section
    in the program list. See the full description of this in content_list.html.
    '''
    programItems = []
    for program in programsList:
        entry = {}
        entry['title'] = create_hyperlink('/academics/' + program.get('name'),
                                          program.get('title'))
        entry['subContent'] = program.get('flavorTextForHeadline')
        programItems.append(entry)
    # Manually add the other academic menu options.
    programItems.append(create_honors_list_entry())
    programItems.append(create_courses_list_entry())
    result = []
    result.append({'sectionItems': programItems})
    return result


def create_honors_list_entry():
    '''This method creates an academic page entry for the honors program.'''
    return {'title': create_hyperlink('/academics/honors', 'Honors Program'),
            'subContent': 'This page gives information on graduating with \
                honors from the Department of Computer Science.'}


def create_courses_list_entry():
    '''This method creates an academic page entry for the course list.'''
    return {'title':
            create_hyperlink('/academics/courses', 'Courses &amp; Materials'),
            'subContent':
            'This page gives links to the department course materials.'}


def create_program_tab_list(program):
    '''This routine maps key elements of the program data from CIT to
    tabs on the program pages. It includes the tabs only if the given
    program data includes the relevant entries.
    '''
    result = []
    if program.get('majorCourses'):
        result.append({'title': 'Major',
                       'primaryContent': program.get('majorCourses')})
    if program.get('modelSchedule'):
        result.append({'title': 'Scheduling',
                       'primaryContent': program.get('modelSchedule')})
    if program.get('minorCourses'):
        result.append({'title': 'Minor',
                       'primaryContent': program.get('minorCourses')})
    if program.get('careers'):
        result.append({'title': 'Careers',
                       'primaryContent': '<p>' + program.get('careers') + '</p>'})
    if program.get('studentInvolvement'):
        result.append({'title': 'Opportunities',
                       'primaryContent': program.get('studentInvolvement')})
    if program.get('scholarships'):
        result.append({'title': 'Scholarships',
                       'primaryContent': program.get('scholarships')})
    return result


def create_course_tab_list(courseList, department):
    '''This routine converts the domain content in the courses list into a
    tablist of rhetorical elements described in includes/content_primary.html.
    Most of the data comes from CIT, but the annual schedule of courses comes
    from the department unit of the local database.
    '''
    if courseList is None:
        return [{'subContent': 'no courses found...'}]
    csCourses = ''
    isCourses = ''
    interimCourses = ''
    for course in courseList:
        courseName = course.get('id')
        # Remove lab courses.
        if courseName.endswith('L'):
            continue
        entry = ''
        link = '/courses/' + course.get('Prefix').lower() + '/' + \
            course.get('Class_Number') + '/'
        description = course.get('Title') + \
            ' (' + course.get('Credit_Hours') + ')'
        entry += create_hyperlink(link, courseName) + \
            ' &ndash; ' + description + '<br>'
        if 'W' in course.get('Class_Number'):
            interimCourses += entry
        elif course.get('Prefix') == 'CS':
            csCourses += entry
        elif course.get('Prefix') == 'IS':
            isCourses += entry
    result = []
    result.append({'title': 'Computer Science',
                   'primaryContent': '<p>' + csCourses + '</p>'})
    result.append({'title': 'Information Systems',
                   'primaryContent': '<p>' + isCourses + '</p>'})
    result.append({'title': 'Interim',
                   'primaryContent': '<p>' + interimCourses + '</p>'})
    result.append({'title': 'Annual Course Schedule',
                   'primaryContent': department.get('courseSchedule')})
    return result


def create_people_list(peopleList):
    '''This routine converts the domain content in the people list into a list
    of rhetorical elements described in includes/content_primary.html. It
    produces a list of dictionaries, one dictionary for each sub-list of
    faculty (i.e., faculty, staff, ...). See the full description of this
    mechanism in content_list.html.
    '''
    if peopleList is None:
        return [{'subContent': 'no people found...'}]
    else:
        peopleList.sort(cmp=None, key=lambda person: person.get('lastName'),
                        reverse=False)
    facultyList = []
    contributingList = []
    emeritiList = []
    staffList = []
    for person in peopleList:
        if is_noncomputing_mathematician(person):
            continue
        # Create a person list entry.
        entry = {}
        entry.update(create_person_image_content(person))
        entry.update(create_person_sub_content(person))
        entry.update(create_person_side_content(person))
        # Add the entry to the correct person list.
        if 'Emeritus' in person.get('jobFunction'):
            emeritiList.append(entry)
        elif 'MATH' in person.get('academicDepartment'):
            contributingList.append(entry)
        elif 'Academic' in person.get('jobFunction'):
            facultyList.append(entry)
        else:
            staffList.append(entry)
    result = []
    result.append({'title': 'Faculty',
                   'sectionItems': facultyList})
    result.append({'title': 'Contributing Faculty',
                   'sectionItems': contributingList})
    result.append({'title': 'Emeriti',
                   'sectionItems': emeritiList})
    result.append({'title': 'Staff',
                   'sectionItems': staffList})
    return result


def is_noncomputing_mathematician(person):
    '''Determine if this person is in the mathematics department and is not
    one of those professors that routinely teach computing-related courses.'''
    return \
        person.get('academicDepartment') == 'MATH' and \
        person.get('lastName') not in ['Pruim', 'Stob', 'Fife']


def create_person_image_content(person):
    '''Create a set of dictionary entries specifying a person's image.'''
    return {
        'image': person.get('image'),
        'imageAlt': 'Professor ' + person.get('lastName') + '\'s picture'
    }


def create_person_sub_content(person):
    '''Create a set of dictionary entries specifying a person's sub-content.'''
    url = 'http://www.calvin.edu/~' + person.get('email')
    full_name = person['firstName'] + ' ' + person['lastName']
    return {
        'title': create_hyperlink(url, full_name),
        'subContent': create_address_entry(person)
    }


def create_person_side_content(person):
    '''Create a set of dictionary entries specifying a person's side-content.
    '''
    sideContent = ''
    if person.get('educationalBackground'):
        sideContent += '<strong>Education</strong>' + \
            person.get('educationalBackground')
    if person.get('academicInterests'):
        sideContent += '<strong>Interests</strong>' + \
            person.get('academicInterests')
    return {'sideContent': sideContent}


def create_address_entry(person):
    '''Build an HTML-formatted address entry for the given person.'''
    return \
        person.get('title') + '<br><br>' + \
        person.get('telephone') + '<br>' + \
        person.get('campusAddress') + ' ' + \
        create_hyperlink('http://www.calvin.edu/map/index.htm?building=NH',
                         'map') + '<br>'


def create_admin_list():
    '''This routine creates a simple administration page with links to the
    basic administration pages.
    '''
    adminItems = []
    adminItems.append(
        {'subContent':
            create_hyperlink(url_for('web.display_admin_programs'),
                             'Programs') +
            ''' - Modify (only the model schedules of) existing programs
            (hard-coded into the academics menu)'''})
    adminItems.append(
        {'subContent':
            create_hyperlink(url_for('web.display_admin_resources'),
                             'Resources') +
            ' - Modify (only) existing resources (hard-coded into the resources menu)'})
    adminItems.append(
        {'subContent':
            create_hyperlink(url_for('web.display_admin_documents'),
                             'Documents') +
            ' - Create, delete or modify documents (linked from existing pages)'})
    adminItems.append(
        {'subContent':
            create_hyperlink(url_for('web.display_admin_images'), 'Images') +
            ' - Create, delete or modify images'})
    adminItems.append(
        {'subContent':
            create_hyperlink(url_for('web.display_admin_news'), 'News Articles') +
            ' - Create, delete or modify news articles'})
    adminItems.append(
        {'subContent':
            create_hyperlink(url_for('web.display_admin_scholarships'), 'Scholarships') +
            ' - Create, delete or modify scholarships'})  
    adminItems.append(
        {'subContent':
            create_hyperlink(url_for('web.display_admin_tech_news'), 'Tech News Articles') +
            ' - Up/down news articles and refresh current list.'}) 
    result = []
    result.append({'sectionItems': adminItems})
    return result


def create_image_list(images):
    '''This routine creates a list of images with update/delete options attached
    to each.
    '''
    imageItems = []
    for image in images:
        item = {}
        item['image'] = '/static/images/' + image.get('filename')
        item['subContent'] = \
            '<strong>' + image.get('name') + '</strong><br>' + \
            image.get('filename') + '<br>' + \
            ', '.join(image.get('tags')) + '<br>' + \
            '<strong>' + create_hyperlink('/images/' + image.get('name') + '/edit', 'Edit') + \
            '</strong> &mdash;' + \
            '<strong>' + create_hyperlink('/images/' + image.get('name') + '/delete', 'Delete') + \
            '</strong>'
        item['sideContent'] = image.get('description')
        imageItems.append(item)
    result = []
    result.append({'sectionItems': imageItems})
    return result


def create_document_list(documents):
    '''This routine creates a list of documents with update/delete options
    attached to each.
    '''
    documentItems = []
    for document in documents:
        item = {}
        documentUrl = '/documents/' + document.get('name')
        item['subContent'] = \
            '<strong>' + document.get('name') + '</strong><br>' + \
            '<strong>' + create_hyperlink(documentUrl, 'Show') + '</strong> &mdash; ' + \
            '<strong>' + create_hyperlink(documentUrl + '/edit', 'Edit') + \
            '</strong> &mdash; ' + \
            '<strong>' + create_hyperlink(documentUrl + '/delete', 'Delete') + \
            '</strong>'
        item['sideContent'] = document.get('title')
        documentItems.append(item)
    result = []
    result.append({'sectionItems': documentItems})
    return result


def create_admin_scholarships_list(scholarships):
    '''This routine creates a list of documents with update/delete options
    attached to each.
    '''
    scholarshipItems = []
    for scholarship in scholarships:
        item = {}
        scholarshipUrl = '/scholarships/' + scholarship.get('name')
        item['subContent'] = \
            '<strong>' + scholarship.get('name') + '</strong><br>' + \
            '<strong>' + create_hyperlink(scholarshipUrl, 'Show') + '</strong> &mdash; ' + \
            '<strong>' + create_hyperlink(scholarshipUrl + '/edit', 'Edit') + \
            '</strong> &mdash; ' + \
            '<strong>' + create_hyperlink(scholarshipUrl + '/delete', 'Delete') + \
            '</strong>'
        item['sideContent'] = scholarship.get('title')
        scholarshipItems.append(item)
    result = []
    result.append({'sectionItems': scholarshipItems})
    return result


def create_scholarships_list(scholarships):
    '''This routine creates a list of scholarship entries.'''
    scholarshipItems = []
    for scholarship in scholarships:
        item = {}
        # Hyperlink the title to either the URL in the CS db or directly to
        # the scholarship page.
        if scholarship.get('url'):
            url = scholarship.get('url')
        else:
            try:
                    url = '/scholarships/' + scholarship.get('name')
            except:
                url = '#'
        item['title'] = create_hyperlink(url, scholarship.get('title'))

        # Add the local shortDescription if it exists.
        if scholarship.get('shortDescription') is not None:
            item['subContent'] = scholarship.get('shortDescription')
        scholarshipItems.append(item)
    result = []
    result.append({'sectionItems': scholarshipItems})
    return result


def create_scholarship_content(scholarship):
    '''This routine creates an entry appropriate for a single scholarship,
    fully described.
    '''
    result = ''
    if scholarship.get('formalDescription'):
        result += '<p>' + scholarship.get('formalDescription') + '</p>'
    if scholarship.get('longDescription'):
        result += '<p>' + scholarship.get('longDescription') + '</p>'
    if scholarship.get('recipients'):
        result += scholarship.get('recipients')
    return result


def create_scholarship_side(scholarship):
    '''This routine creates an entry appropriate for a single scholarship,
    fully described.
    '''
    result = ''
    if scholarship.get('maximumAmount'):
        result += '<b>Award Amount:</b> ' + scholarship.get('maximumAmount')
        result += '<br>'
    if scholarship.get('classAvailability'):
        result += '<b>Class Level:</b> '
        result += fix_class_value(scholarship.get('classAvailability'))
        result += '<br>'
    if scholarship.get('gpatext'):
        result += '<b>Minimum GPA:</b> '
        result += scholarship.get('gpatext')
        result += '<br>'
    if scholarship.get('needpref') is not None:
        if scholarship.get('needpref') == 'TRUE':
            result += '<b>Financial need?:</b> Required<br>'
        elif scholarship.get('needpref') == 'CONSIDERED':
            result += '<b>Financial need?:</b> Preferred<br>'
        else:
            result += '<b>Financial need?:</b> Not considered<br>'
    if scholarship.get('applicationprocess'):
        result += capitalize(scholarship.get('applicationprocess'))
    if scholarship.get('appInfo'):
        result += scholarship.get('appInfo')
    return result


def fix_class_value(value):
    '''This method removes the trailing comma and (sometimes) space that
    CIT includes in their class availability fields.'''
    p = re.compile(', *$')
    return p.sub('', value)


def create_resources_list(resourcesList):
    '''This routine converts the domain content in the resources list into a
    list of rhetorical elements described in includes/content_primary.html.
    See the full description of this in content_list.html.

    External resources that are linked directly don't get the default,
    hyperlinked titles.
    '''
    resourceItems = []
    for resource in resourcesList:
        entry = {}
        if resource.get('name') in ['club', 'listservs',
                                    'calvin_student_resources']:
            # External resources are linked manually.
            entry['title'] = resource.get('title')
        else:
            entry['title'] = \
                create_hyperlink('/resources/' + resource.get('name'),
                                 resource.get('title'))
        entry['subContent'] = resource.get('summary')
        resourceItems.append(entry)
    result = []
    result.append({'sectionItems': resourceItems})
    return result


def create_resource_tab_list(resource):
    '''This routine maps tabbed elements of the resource unit to
    tabs on the resource pages. It includes the tabs only if the given
    resource unit includes the relevant entries (contentTab1-3).

    This mechanism is a hack that assumes no more than three tabs for
    resource pages. Supporting an arbitrarily-long tab list would be more
    expandable, but would require adding support for editing tab list elements.
    '''
    result = []
    if resource.get('contentTab1'):
        result.append({'title': resource.get('contentTab1Title'),
                       'primaryContent': resource.get('contentTab1')})
    if resource.get('contentTab2'):
        result.append({'title': resource.get('contentTab2Title'),
                       'primaryContent': resource.get('contentTab2')})
    if resource.get('contentTab3'):
        result.append({'title': resource.get('contentTab3Title'),
                       'primaryContent': resource.get('contentTab3')})
    return result


def create_admin_resources_list(resources):
    '''This routine creates a list of resource units with only the update
    option attached to each. This is only for administrators.
    '''
    resourceItems = []
    for resource in resources:
        item = {}
        resourceUrl = '/resources/' + resource.get('name')
        item['subContent'] = \
            '<strong>' + resource.get('name') + '</strong><br>' + \
            '<strong>' + create_hyperlink(resourceUrl, 'Show') + \
            '</strong> &mdash; ' + \
            '<strong>' + create_hyperlink(resourceUrl + '/edit', 'Edit')
        item['sideContent'] = \
            resource.get('title') + '<br><p>' + resource.get('summary') + \
            "</p>"
        resourceItems.append(item)
    result = []
    result.append({'sectionItems': resourceItems})
    return result


def create_admin_programs_list(programs):
    '''This routine creates a list of program units with only the update
    option attached to each. This is only for administrators.
    '''
    programItems = []
    for program in programs:
        item = {}
        resourceUrl = '/academics/' + program.get('name')
        item['subContent'] = \
            '<strong>' + program.get('name') + '</strong><br>' + \
            '<strong>' + create_hyperlink(resourceUrl, 'Show') + '</strong> &mdash; ' + \
            '<strong>' + create_hyperlink(resourceUrl + '/edit', 'Edit')
        item['sideContent'] = \
            program.get('title') + '<br><p>' + program.get('name') + "</p>"
        programItems.append(item)
    result = []
    result.append({'sectionItems': programItems})
    return result


def create_newsarticle_list(news_articles):
    '''This routine creates a list of news news_articles with update/delete options
    attached to each.
    '''
    articles = []
    for article in news_articles:
        if article.get('name').startswith('tech_news'):
            item = {}
            documentUrl = '/news/' + article.get('name')
            item['subContent'] = \
                '<div class = "article">'+ \
                '<strong>' + article.get('name') + '</strong><br>' + \
                '<strong>' + create_hyperlink(documentUrl, 'Show') + '</strong> &mdash; ' + \
                '<strong>' + '<input type = "submit" value = "Up" class = "updateNews" name = "/admin/technews/' + article.get('summary').replace('/','').replace('?','') + '/up/refresh"></input>' + \
                '</strong> &mdash; ' + \
                '<strong>' + '<input type = "submit" value = "Down" class = "updateNews" name = "/admin/technews/' + article.get('summary').replace('/','').replace('?','') + '/down/refresh"></input>' + \
                '</strong></div>'
            item['sideContent'] = article.get('title')
            articles.append(item)
        else:
            item = {}
            documentUrl = '/news/' + article.get('name')
            item['subContent'] = \
                '<strong>' + article.get('name') + '</strong><br>' + \
                '<strong>' + create_hyperlink(documentUrl, 'Show') + '</strong> &mdash; ' + \
                '<strong>' + create_hyperlink(documentUrl + '/edit', 'Edit') + \
                '</strong> &mdash; ' + \
                '<strong>' + create_hyperlink(documentUrl + '/delete', 'Delete') + \
                '</strong>'
            item['sideContent'] = article.get('title')
            articles.append(item)
    result = []
    result.append({'sectionItems': articles})
    return result


def create_techNewsarticle_list(news_articles):
    '''This routine creates a list of news news_articles with update/delete options
    attached to each.
    '''
    articles = []
    for article in news_articles:
        item = {}

        documentUrl = article.get('links')[0].get('href')
        # Skip cases where there is no href specified. -kvlinden, 31man2016
        if documentUrl == None:
            break
        item['subContent'] = \
            '<div class = "article">' + \
            '<strong>' + article.get('title') + '</strong><br>' + \
            '<strong>' + create_hyperlink(documentUrl, 'Show') + '</strong> &mdash; ' + \
            '<strong>' + '<input type = "submit" value = "Up" class = "updateNews" name = "/admin/technews/' + documentUrl.replace('/', '').replace('?', '') + '/up"></input>' + \
            '</strong> &mdash; ' + \
            '<strong>' + '<input type = "submit" value = "Down" class = "updateNews" name = "/admin/technews/' + documentUrl.replace('/', '').replace('?', '') + '/down"></input>' + \
            '</strong></div>'
        item['sideContent'] = article.get('summary')
        articles.append(item)
    result = []
    result.append({'sectionItems': articles})
    return result


# ---------------------------------------------------------------------------
# Basic utilities...


def check_unit(item):
    '''Throw an HTTP 404 error for units that cannot be found.'''
    if item is None:
        abort(404)
    return item


def get_breadcrumbs(*args):
    '''This routine creates a list of tuples for use in creating a breadcrumb
    trail, where the tuples are of the form (page name, hyperlink). It always
    adds a link for the home page (/) on the front and always sets the last
    page as the current page (#). It takes an arbitrary number of arguments,
    which it assumes to be an ordered list of super-pages not including home.
    '''
    result = [('Home', '/')]
    url = ''
    for i in range(0, len(args) - 1):
        if args[i] is not None:
            url += '/' + args[i]
            result.append((capitalize(args[i]), url))
    result.append((capitalize(args[len(args) - 1]), '#'))
    return result


def get_name(superpage, name):
    '''This routine returns the full name of the webpage resource for the given
    superpage/name pair. The page names include the full path to the resource
    with at most one level of subordination.
    '''
    if superpage:
        return superpage + '/' + name
    else:
        return name


def get_today():
    '''Gets today's date in a standard format.'''
    return datetime.today()


def format_date(date):
    '''Returns the given date as a formatted string'''
    return date.strftime('%B %d, %Y')


def get_counter(collection):
    '''Get the next, unique count for the given collection.'''
    counter_record = g.mongo.db.counters.find_one({'name': collection})
    count = counter_record['count']
    counter_record['count'] = count + 1
    g.mongo.db.counters.save(counter_record)  # @UndefinedVariable
    return count


def create_hyperlink(url, destination):
    '''Create an HTML anchored hyperlink from the given destination text to the
    given URL. Mark external links appropriately.
    '''
    if url.startswith('/'):
        anchor = '<a href="' + url + '">'
    else:
        anchor = '<a href="' + url + '" class="external">'
    return anchor + destination + '</a>'


def capitalize(s):
    return s[:1].upper() + s[1:]


def is_logged_in():
    '''This method determines if the user is logged in as an administrator.'''
    return session.get('logged_in', False)


def is_safe_url(target):
    '''This method checks that the target URL is safe. It is copied from:
        http://flask.pocoo.org/snippets/62/
    '''
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
        ref_url.netloc == test_url.netloc


def is_admin_page(page):
    '''This routine determines if the given page is an administration page,
    which requires login. All administration pages and all edit/create pages
    require administrative access.
    '''
    if page is None:
        return False
    path = urlparse(page).path
    return path.startswith('/admin') or \
        path.endswith('create') or \
        path.endswith('edit') or \
        path.endswith('delete')

ERROR_404_MESSAGE = '''<div class="row">
         <div class="large-4 medium-4 columns show-for-medium-up">
         <img
           src="http://www.calvin.edu/global/error-pages/404-error-joust.png"
           alt="Oh, snap!"/>
         </div>
         <div class="large-8 medium-8 columns">
           <h3>HTTP Error: 0b110010100</h3>
           <p>Sorry, the page you&rsquo;re looking for cannot be found.
           <br>Try going back or choosing a different option.</p>
         </div>
       </div>
       '''
