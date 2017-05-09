'''
This data structure provides a hard-coded starting point for development.
All collections have unique id values.

Changing the structure of this development database requires changing
utils.db accordingly.

Created on Jan 23, 2014

@author: kvlinden
'''
from datetime import datetime

from passlib.apps import custom_app_context


data = [

    # programs...
    [
{'name': 'csm'},{'name': 'ism'},{'name': 'dsm'},{'name': 'dam'},{'name': 'dcm'},
         {'name': 'bcs',
          'modelSchedule': '''
<p>The following course schedule provides a suggested framework for students pursuing the <span class="caps">BCS</span> degree, assuming that they have had some high school language and will do a senior project (instead of an internship).  Any exemptions a student can bring from high school would increase the flexibility of this schedule.</p>
<table border="1" class="degree">
<tr><th>Year</th><th>Fall</th><th>Interim</th><th>Spring</th></tr>
<tr><th>Freshman</th><td> <ul><li><a href="/courses/cs/108/" title="CS 108: Introduction to Computing">CS 108</a></li>
<li><span class="caps">MATH</span> 171</li>
<li>FL 121</li>
<li><span class="caps">IDIS</span> 149</li>
<li>core</li>
<li><a href="/courses/cs/x95" title="CS 195: Introductory Computing Seminar">CS 195</a></li>
<p></ul> </td>
<td> <ul><li>FL 122</li></p>
<p></ul> </td>
<td> <ul><li><a href="/courses/cs/112/" title="CS 112: Introduction to Data Structures">CS 112</a></li>
<li><span class="caps">MATH</span> 172</li>
<li>FL 123</li>
<li><span class="caps">IDIS</span> 150</li>
<li><a href="/courses/cs/x95" title="CS 195: Introductory Computing Seminar">CS 195</a></li></p>
<p></ul> </td></p>
<p></tr><tr><th>Sophomore</th><td> 
<ul><li><a href="/courses/cs/212/" title="CS 212: Data Structures and Algorithms">CS 212</a></li>
<li><span class="caps">MATH</span> 156</li>
<li><span class="caps">ENGR</span> 220</li>
<li>core</li>
<li><a href="/courses/cs/x95" title="CS 195: Introductory Computing Seminar">CS 195</a></li></p>
<p></ul> </td>
<td> <ul><li>core</li></p>
<p></ul> </td></p>
<td> <ul><li><a href="/courses/cs/214/" title="CS 214: Programming Languages">CS 214</a></li>
<li><span class="caps">MATH</span> 256</li>
<li><span class="caps">CAS</span> 101</li>
<li>core</li>
<li>PE core</li>
<p></ul> </td></p>
<p></tr><tr><th>Junior</th><td> <ul><li><a href="/courses/cs/262/" title="CS 262: Software Engineering">CS 262</a></li>
<li>CS/IS elective</li>
<li><span class="caps">SCI</span> elective</li>
<li>core</li>
<li>core</li>
<li><a href="/courses/cs/x95/" title="CS 295: Computing Seminar">CS 295</a></li></p>
<p></ul> </td></p>
<td> <ul><li>CS/IS elective</li>
<p></ul> </td>
<td> <ul><li><a href="/courses/cs/232/" title="CS 232: Operating Systems and Networking">CS 232</a></li>
<li><span class="caps">SCI</span> elective</li>
<li><span class="caps">MATH</span> 243</li>
<li>core</li>
<li>PE core</li>
<li><a href="/courses/cs/x95/" title="CS 295: Computing Seminar">CS 295</a></li></p>
<p></ul> </td></p>
<p></tr><tr><th>Senior</th><td> <ul><li><a href="/courses/cs/396/" title="CS 396: Senior Project I">CS 396</a></li>
<li>CS/IS elective</li>
<li><span class="caps">SCI</span> elective</li>
<li>core</li>
<li>core</li>
<li><a href="/courses/cs/x95/" title="CS 295: Computing Seminar">CS 295</a></li></p>
<p></ul> </td></p>
<td> &nbsp; </td>
<td> <ul><li><a href="/courses/cs/398/" title="CS 398: Senior Project II">CS 398</a></li>
<li>CS/IS elective</li>
<li><a href="/courses/cs/384/" title="CS 384: Perspectives on Computing">CS 384</a></li>
<li>core</li>
<li>core</li>
<li>PE core</li>
<p></ul> </td></p>
</tr></table>
'''
      },
     {'name': 'cs',
      'modelSchedule': '''
<p>The following course schedule provides a suggested framework for students pursuing a BA (or BS) in CS.</p>
<table border="1" class="degree">
<tr><th>Year</th><th>Fall</th><th>Interim</th><th>Spring</th></tr>
<tr><th>Freshman</th><td> <ul><li><a href="/courses/cs/108/" title="CS 108: Introduction to Computing">CS 108</a></li>
<li><a href="/courses/cs/x95" title="CS 195: Introductory Computing Seminar">CS 195</a></li>
<li><span class="caps">MATH</span> 171</li>
<p></ul> </td>
<td> &nbsp; </td>
<td> <ul><li><a href="/courses/cs/112/" title="CS 112: Introduction to Data Structures">CS 112</a></li><li><a href="/courses/cs/x95" title="CS 195: Introductory Computing Seminar">CS 195</a></li>
<li><span class="caps">MATH</span> 172*</li></p>
<p></ul> </td></p>
</tr>
<tr><th>Sophomore</th><td> <ul><li><a href="/courses/cs/212/" title="CS 212: Data Structures and Algorithms">CS 212</a></li>
<li><a href="/courses/cs/x95" title="CS 195: Introductory Computing Seminar">CS 195</a></li>
<li><span class="caps">MATH</span> 156</li>
<li><span class="caps">ENGR</span> 220</li>
<p></ul> </td>
<td> &nbsp; </td>
<td> <ul><li><a href="/courses/cs/214/" title="CS 214: Programming Languages">CS 214</a></li>
<li><span class="caps">MATH</span> 256</li></p>
<p></ul> </td></p>
<p></tr><tr><th>Junior</th><td> <ul><li><a href="/courses/cs/262/" title="CS 262: Software Engineering">CS 262</a><sup></sup></li>
<li>CS/IS elective</li>
<li><a href="/courses/cs/x95/" title="CS 295: Computing Seminar">CS 295</a></li></p>
<p></ul> </td>
<td> <ul><li>CS/IS elective</li></p>
<p></ul> </td>
<td> <ul><li><a href="/courses/cs/232/" title="CS 232: Operating Systems and Networking">CS 232</a></li><li><a href="/courses/cs/x95/" title="CS 295: Computing Seminar">CS 295</a></li>
<li><span class="caps">MATH</span> 243*</li></p>
<p></ul> </td></p>
<p></tr><tr><th>Senior</th><td> <ul><li><a href="/courses/cs/394/" title="CS 394: Internship ">CS 394</a> or <a href="/courses/cs/396/" title="CS 396: Senior Project I">CS 396</a></li></p>
<li>CS/IS elective</li><li><a href="/courses/cs/x95/" title="CS 295: Computing Seminar">CS 295</a></li>
<p></ul> </td>
<td> &nbsp; </td>
<td> <ul><li><a href="/courses/cs/394/" title="CS 394: Internship ">CS 394</a> or <a href="/courses/cs/398/" title="CS 398: Senior Project II">CS 398</a></li>
<li><a href="/courses/cs/384/" title="CS 384: Perspectives on Computing">CS 384</a></li></p>
<p></ul> </td></p>
<p></tr></table></p>
<p><sup>*</sup> <span class="caps">MATH</span> 171, 172, and 243 are preferred, but students may choose to take <span class="caps">MATH</span> 143 and 171 or <span class="caps">MATH</span> 143 and 132 instead.</p>'''
      },
      {'name': 'is',
      'modelSchedule': '''
<p>The following course schedule provides a suggested framework for students pursuing this degree.</p>
<table border="1" class="degree">
<tr><th>Year</th><th>Fall</th><th>Interim</th><th>Spring</th></tr>
<tr><th>Freshman</th><td> <ul>
<li><a href="/courses/cs/108/" title="CS 108: Introduction to Computing">CS 108</a></li>
<li><span class="caps">MATH</span> 143</li>
<li><a href="/courses/cs/x95" title="CS 195: Introductory Computing Seminar">CS 195</a></li>
<p></ul> </td>
<td> &nbsp; </td>
<td> <ul>
<li><a href="/courses/cs/112/" title="CS 112: Introduction to Data Structures">CS 112</a></li>
<li><span class="caps">BUS</span> 160</li>
<li><a href="/courses/is/171/" title="IS 171: Computing with Spreadsheets">IS 171</a></li>
<li><a href="/courses/cs/x95" title="CS 195: Introductory Computing Seminar">CS 195</a></li></p>
<p></ul> </td></p>
<p></tr><tr><th>Sophomore</th><td> <ul>
<li><a href="/courses/is/271/" title="IS 271: Introduction to Information Systems">IS 271</a></li>
<li><a href="/courses/is/141/" title="IS 141: Computing with Databases">IS 141</a></li>
<li><span class="caps">BUS</span> 203</li>
<li><a href="/courses/cs/x95" title="CS 195: Introductory Computing Seminar">CS 195</a></li></p>
<p></ul> </td>
<td> &nbsp; </td>
<td> <ul><li><span class="caps">ECON</span> 221</li>
<li><span class="caps">MATH</span> 201</li></p>
<p></ul> </td></p>
<p></tr><tr><th>Junior</th><td> <ul>
<li><a href="/courses/cs/262/" title="CS 262: Software Engineering">CS 262</a></li>
<li>IS/CS elective</li>
<li><a href="/courses/cs/x95/" title="CS 295: Computing Seminar">CS 295</a></li></p>
<p></ul> </td>
<td> &nbsp; </td>
<td> <ul><li>IS/CS elective</li>
<li><span class="caps">BUS</span>/<span class="caps">ECON</span> elective</li>
<li><a href="/courses/cs/x95/" title="CS 295: Computing Seminar">CS 295</a></li></p>
<p></ul> </td></p>
<p></tr><tr><th>Senior</th><td> <ul>
<li><a href="/courses/is/341/" title="IS 341: Database Administration">IS 341</a></li>
<li><span class="caps">BUS</span>/<span class="caps">ECON</span> elective</li>
<li><span class="caps">BUS</span> 359 or <a href="/courses/cs/394/" title="CS 394: Internship ">CS 394</a></li>
<li><a href="/courses/cs/x95/" title="CS 295: Computing Seminar">CS 295</a></li></p>
<p></ul> </td>
<td> &nbsp; </td></p>
<td> <ul><li><a href="/courses/is/371/" title="IS 371: Information Systems Leadership">IS 371</a></li>
<li><a href="/courses/cs/384/" title="CS 384: Perspectives on Computing">CS 384</a></li>
<p></ul> </td></p>
<p></tr></table>
'''      
      },
        {'name': 'dc'
         },
        {'name': 'ds'
         },

        {'name': 'da',
      'title': 'Digital Art',
      'flavorTextForHeadline': '''Calvin&rsquo;s BA in digital art
                is designed for students who have broad interests
                in the arts and digital media.''',
      'longDescription': '''<p>Any student at Calvin College has the option of
      designing their own interdisciplinary major; this major must be approved
      by the departments from which you draw your courses.
Since different people have different interests,
the Computer Science and Art Departments worked together to create <em>two</em>
possible ways to construct an interdisciplinary major in Art and Computer
Science. Other colleges might call this major program &#8220;Digital
Art&#8221;, &#8220;Digital Imaging&#8221;, or &#8220;Digital Media&#8221;.</p>
''',
     'majorCourses': '''
<p>Both tracks have a common kernel of courses that you must take:</p>
<ul>
<li>Art 153 (Visual Culture, core)</li>
<li>Art Studio 250 (Intro to Drawing)</li>
<li>Art Studio 255 (Communication Design I)</li>
<li>Art Studio 305 (Communication Design II)</li>
<li>Art Studio 355 (Communication Design <span class="caps">III</span>)</li>
<li>Art History 240 (Contemporary Art, core)</li>
<li>Computer Science 108 (Intro to Computing)</li>
<li>Computer Science 384 (Perspectives on Computing, core)</li>
<li>Information Systems 141 (Computing with Databases)</li>
<li>Information Systems 151 (Computing Presentations)</li>
<li>Information Systems 153 (Computing with the Internet)</li>
<li>Information Systems 337 (Website Administration)</li>
<li>Information Systems 341 (Database Administration)</li>
</ul>
<p>Then pick your emphasis:</p>
<table>
<tr>
<th style="width: 50%">Computer Graphics Emphasis</th>
<th style="width: 50%">Multimedia Emphasis</th>
</tr>
<tr>
<td style="vertical-align: top">
<ul>
<li>Computer Science 112 (Data Structures with C++)</li>
<li>Computer Science 212 (Algorithms and Data Structures)</li>
<li>Computer Science 352 (Computer Graphics)</li>
<li>An approved interim</li>
<li>Mathematics 156 (Discrete Mathematics for CS)</li>
<li>Mathematics 256 (Discrete Structures and Linear Algebra)</li>
</ul>
</td>
<td style="vertical-align: top">
<ul>
<li>Art Studio 256 (Intro to Photography)</li>
<li>Art Studio 316 (Digital Photography)</li>
<li>Art Studio 300 (Intermediate Drawing)</li>
<li>Information Systems 271 (Intro to IS)</li>
<li><span class="caps">CAS</span> 190 (Video Production I)</li>
<li><span class="caps">CAS</span> 250 (TV Studio Production)</li>
</ul>
</td>
</tr>
</table>
<p>In addition to the courses in your particular emphasis, you are encouraged
to take courses from the other emphasis.  You are free to swap alternative
courses for those listed above; however, student programs that deviate from
the course sequences above require advisor <em>and departmental approval</em>.
<p>
By contrast, the course sequences described above have already been approved
by both the CS and Art departments, so a student program consisting of those
sequences requires no special action beyond the approval of your advisor.</p>
''',
      'careers': '''BA majors are prepared to pursue a variety of careers, including:
<ul>
<li>Graphic design</li>
<li>Web development</li>
<li>Multimedia production</li>
<li>Marketing designer</li>
</ul>
''',
'studentInvolvement': '''Work in business development; gain real-world experience
during a summer internship; write for the Chimes or Dialogue.''',
       'schedule': None
      },

     {'name': 'base',
      'title': 'Minor in Computer Science for Secondary Education',
      'shortDescription': '''
  <p>The minor program in computer science for students majoring in secondary
  education covers the core elements of computer science required by state and
  national teachers accreditation commissions.  All of our education majors
  with the CS specialization have passed their boards.</p>
    ''',
      'minor': '''
<ul>
    <li>IS 141</li>
    <li>IS 171</li>
    <li>IS 271</li>
    <li>CS 100</li>
    <li>CS 108</li>
    <li>CS 112</li>
    <li>CS 212</li>
    <li><span class="caps">EDUC</span> W10</li>
</ul>
      '''
      }
     ],

    # documents...
    [{'name': 'computing_careers',
      'title': 'The Market for Computing Careers',
      'content': '''
        <p>There are lots of myths about computing careers.
One of the most ridiculous is the myth that all the computing jobs are going
overseas.
According to this
<a
href="http://www.informationweek.com/global-cio/outsourcing/outsourcings-new-reality-choice-beats-co/240006048">recent
Information Week article</a>,
the majority of the work that U.S. companies are &#8220;outsourcing&#8221;
is actually going to companies here in the U.S.,
as can be seen in this chart from that article:
<p>
 <img src="http://cs.calvin.edu/images/department/jobs/2020/0.InfoWeek-Outsourcing.jpg" 
          width="580" height="362"
          alt="Information Week indicates that 60% of the outsourced work is to U.S. companies.">
<p>
The problem is that many mainstream media writers use the following terms interchangeably:
<ul>
<li>
<strong>outsourcing</strong>, that is, sending work to a different <em>company</em>.</li>
<li>
<strong>offshoring</strong>, that is, sending work to a different <em>country</em>. </li></p>
</ul>
<p>Since many companies are outsourcing their software development, this creates the false impression that those companies are sending that work overseas.
As the preceding chart indicates, the majority of the outsourced work is staying here in the U.S., and the indications are that the number of computing jobs will continue to grow faster than most other sectors.
<p>
To see why, consider that the
<a href="http://www.bls.gov/emp/">U.S. Bureau of Labor Statistics</a> (US-<span class="caps">BLS</span>) predicts that computing will be one of the fastest-growing U.S. job markets in science, technology, engineering, and mathematics (<span class="caps">STEM</span>) for the foreseeable future, as indicated on the following chart:
<p>
<a href="http://cs.calvin.edu/images/department/jobs/2020/1.US_BLS_AnnualNewJobs-2020.png"
target="_blank">
 <img src="http://cs.calvin.edu/images/department/jobs/2020/1.US_BLS_AnnualNewJobs-2020.png" 
          width="650" height="748"
          alt="The U.S. Bureau of Labor Statistics predicts that the top five fastest growing STEM jobs between now and 2020 are all in computing."></a>
<center>
(Click on the chart for a larger image.)</p>
</center>
<p>As you can see, the US government is predicting that the five fastest-growing <span class="caps">STEM</span> jobs will all be in computing; only one other area (civil engineering) is expected to generate more than 5000 new jobs per year.  By contrast, <strong>the US-<span class="caps">BLS</span> predicts there will be over 31,000 software engineering jobs, over 12,000 systems analysts jobs, 11,000 computing support jobs, and over 9,000 network/systems administration jobs, and over 6,000 computer security, web developer, or network architect jobs, each year.</strong></p>
<p>
If we aggregate the US-<span class="caps">BLS</span> numbers as percentages by <span class="caps">STEM</span> area, we get the following chart:  
<p>
<a href="http://cs.calvin.edu/images/department/jobs/2020/2.US_BLS_STEM_Percentages-2020.png"
target="_blank">
<img src="http://cs.calvin.edu/images/department/jobs/2020/2.US_BLS_STEM_Percentages-2020.png" 
border="3" 
width="687" height="408"
alt="The U.S. Bureau of Labor predicts that between now and 2020, 73% of the new STEM jobs will be computing jobs"></a></p>
<!---
<a href="http://cs.calvin.edu/images/department/jobs/STEM-Jobs-2018-652x436.png"
target="_blank">
<img src="http://cs.calvin.edu/images/department/jobs/STEM-Jobs-2018-505x337.png" border="3" alt="The U.S. Bureau of Labor predicts that between now and 2018, 71% of the new jobs in science and engineering will be computing jobs"></a>
--></p>
</p>
<center>
<p>(Click on the chart for a larger image.)</p>
</center>
<p>
<p>For the foreseeable future,
<strong>
nearly 3 out of 4 new science, technology, engineering, or mathematics jobs in the U.S. are going to be in computing!
</strong>
By contrast, just 16% will be traditional engineering jobs, and even fewer will be in the sciences or mathematics.
<p>
What kind of &#8220;computing&#8221; jobs are these?  The bar-chart on the right breaks the &#8220;computing&#8221; jobs down in the different career categories, and shows the variety of careers that are available for students who study computing.  
As can be seen, the US-<span class="caps">BLS</span> is predicting that <strong>30% (314,600) of the new <span class="caps">STEM</span> jobs will be in software development (aka software engineering) alone as compared to 16% (178,400 jobs) in the combined branches of traditional engineering!</strong></p>
<p>
Why so many software development/engineering jobs?
In a nutshell, the reason is the <em>mobile computing market</em>.
Every organization wants apps for the iPhone and iPad, which run Apple&#8217;s iOS operating system, 
and for all the phones and tablets running the Android operating system.
These organizations also want a modern web presence, which requires web development and database expertise.
Together, these are creating a huge demand for people to build and maintain those apps, websites, and databases.
<p>
Note that basic computer literacy (i.e., knowing Microsoft Word, Excel, or Powerpoint) or <span class="caps">CAD</span>-design will <em>not</em> qualify you for one of these jobs.
These jobs require advanced computing skills in modern software development that you will only gain by studying computer science, information systems, and/or software engineering.</p>
<p>
With all of these jobs out there, you&#8217;d expect
students to be flocking to computing.
Unfortunately, the opposite has been true until recently, as the following chart shows:
<p>
<a href="http://cs.calvin.edu/images/department/jobs/2020/4.CRA-Taulbee-CS-Bachelors.png"
target="_blank">
<img src="http://cs.calvin.edu/images/department/jobs/2020/4.CRA-Taulbee-CS-Bachelors.png" 
border="3" 
width="693"
height="400"
alt="Nationwide, computer science enrollments declined roughly 50% between 2002 and 2009"></a></p>
</p>
<p><!---
<a href="http://cs.calvin.edu/images/department/jobs/CS-Grads-97-07-small.png"
target="_blank">
<img src="http://cs.calvin.edu/images/department/jobs/CS-Grads-97-07-505x421.png" border="3" alt="Nationwide, computer science enrollments declined roughly 50% between 2002 and 2007"></a>
-->
<center>
(Click on the chart for a larger image.)</p>
</center>
<p>
<p>So the demand for computing-related professionals is exploding, but until recently, fewer students have been choosing to study the subjects needed to pursue these careers.
As a result of this supply-demand imbalance, salaries for these professionals are climbing.
To see current ranges, check out these salaries for  
<a href="http://money.usnews.com/money/careers/articles/2012/02/27/best-jobs-2012-software-developer" target="_blank">software developers</a>, 
<a href="http://money.usnews.com/money/careers/articles/2012/02/27/best-jobs-2012-database-administrator" target="_blank">database administrators</a>, 
<a href="http://money.usnews.com/money/careers/articles/2012/02/27/best-jobs-2012-web-developer"
target="_blank">web developers</a>, and
<a href="http://money.usnews.com/money/careers/articles/2012/02/27/best-jobs-2012-computer-systems-analyst" target="_blank">systems analysts</a>, 
which <strong>U.S. News &amp; World Report</strong> ranked as its 
#1, #2, #3, and #4 
<em>Best Science and Technology</em> jobs for 2012.
<p>
If that&#8217;s not enough to convince you, the following chart compares the total projected jobs in the various <span class="caps">STEM</span> categories against the number of bachelors degrees currently being awarded in those categories:
<p>
<a href="http://cs.calvin.edu/images/department/jobs/2020/3.US_BLS_STEM_JobsVsGrads-2020.png" target="_blank">     
<img src="http://cs.calvin.edu/images/department/jobs/2020/3.US_BLS_STEM_JobsVsGrads-2020.png" 
border="5" 
width="698"
height="384"
alt="Nationwide, there is an oversupply of graduates in every field except computer science">
     </a></p>
</p>
<p><!---
<a href="http://cs.calvin.edu/images/department/jobs/JobsVsGrads-2018-665x454.png" target="_blank">
     <img src="http://cs.calvin.edu/images/department/jobs/JobsVsGrads-2018-503x343.png" border="5" alt="Nationwide, there is an oversupply of graduates in every field except computer science">
     </a>
-->
<center>
(Click on the chart for a larger image.)</p>
</center>
<p>
<p>The yellow bars indicate the total number of job openings projected in each area per year,
and the orange bars indicate the current number of graduates in those areas.
In engineering, the sciences, and mathematics, 
there are more graduates than there are jobs.
If graduation levels remain the same, 
this means the graduates from these programs will be competing for the available jobs, 
which tends to keep salaries flat.
<p> 
But in computing, there is a huge undersupply of graduates.
As in any situation where demand exceeds supply, companies are competing for the (relatively few) available graduates that have advanced computing skills, driving salaries up.
This is creating a &#8220;perfect storm&#8221; for people with degrees in computing-related fields, as they have a wealth of career options from which to choose.</p>
<hr>
<p>
<p>If you are still skeptical, our final chart shows the number of requests Calvin&#8217;s CS Department has 
received each month from January 2003 though March 2012 
from companies seeking students with advanced computing skills:
<p>
<a href="http://cs.calvin.edu/images/department/jobs/2020/5.Calvin_CS_Job_Requests_2003-2012.png" target="_blank">     
<img src="http://cs.calvin.edu/images/department/jobs/2020/5.Calvin_CS_Job_Requests_2003-2012.png" 
border="5" 
width="698"
height="278"
alt="Calvin computer science students are in high demand">
     </a></p>
</p>
<center>
<p>(Click on the chart for a larger image.)</p>
</center>
<p>
<p>These include both full-time positions and (mostly paid) student internships.
The average wage for the paid internships is about $15/hr.
<p>
As can be seen from the ascending trend line, the average number of requests received by our department has grown to the point that, as of March 2012, it is approaching 4 requests per week, with the majority of these requests being for software developers or web developers. 
Moreover, this growth in demand has continued through the &#8220;Great Recession&#8221; of 2009 and 2010.
<p>
Why?  
Because this is the 21<sup>st</sup> century, software controls much of our day-to-day lives, 
and people are needed to create and maintain that software.
To prepare students for this century, Calvin&#8217;s 
<a href="http://cs.calvin.edu">Department of Computer Science</a> offers:
<ul>
<li>
 a computing education that is
<a href="http://cs.calvin.edu/p/MFT_Results">measurably a top program, nationally</a>;
 <li> 
strong computing programs, including our
  <a href="http://abet.org"><span class="caps">ABET</span></a>-accredited 
  <a href="http://cs.calvin.edu/p/bcs"><span class="caps">BCS</span> program</a> and
  BA/BS degrees in
 <ul>
  <li>
  <a href="http://cs.calvin.edu/academics/cs">computer science</a>,</li>
  <li>
  <a href="http://cs.calvin.edu/academics/is">information systems</a>, </li>
  <li>
  <a href="http://cs.calvin.edu/p/ds">data science</a>, and</li>
  <li>
  <a href="http://cs.calvin.edu/p/dc">digital communication</a>;</li></p>
</ul>
<li>
an excellent <a href="http://cs.calvin.edu/people">faculty</a>,</li>
<li>
<p>outstanding
<a href="http://cs.calvin.edu/p/facilities">facilities</a>,</li>
<li>
<a href="http://cs.calvin.edu/p/research">undergraduate research opportunities</a>, and</li> 
<li> 
<a href="http://cs.calvin.edu/p/christian_scholarship">a distinctively Christian approach
to computer science</a>.</li></p>
</ul>
<p>
<p>If God has gifted you with creative, logical, and/or quantitative abilities, He may be calling you
to a career in computing.  We invite you to join us &#8212;
we will do everything we can to help you explore that calling.</p>
      '''
      }],
    
    # resources...
    [
     
     {'name': 'news',
      'ordinal': 0,
      'title': 'News and Events',
      'summary': 'A set of articles on department news and events.',
      'date': datetime.strptime('2014-9-1', '%Y-%m-%d')
      },
     
     {'name': 'faqs',
      'ordinal': 1,
      'title': 'Frequently-Asked Questions',
      'summary': 'Questions commonly asked by current or incoming students',
      'contentTab1Title': 'Incoming Students',
      'contentTab1': '''<p>There are many questions you may have about choosing a
discipline and choosing a college. This FAQ addresses the computer
science and information systems options at Calvin College. Please
do not hesitate to contact us if there are other questions you have
(see the last question in this FAQ).</p>

<a name="topi"></a><h2>Questions</h2><ul class="faqlist">
<li><a href="#0i" class="faqitem">What is computing?</a></li>
<li><a href="#1ai" class="faqitem">Aren't the computing jobs all going to India?</a></li>
<li><a href="#1i" class="faqitem">Doesn't computing just focus on programming?</a></li>
<li><a href="#2i" class="faqitem">What kinds of jobs are there for computer scientists?</a></li>
<li><a href="#3i" class="faqitem">Won't I end up working at a computer in a cubicle the rest of my life like Dilbert?</a></li>
<li><a href="#4i" class="faqitem">Does Calvin have a good computing program?</a></li>
<li><a href="#5i" class="faqitem">I'm interested in computing; what can I do to get started?</a></li>
<li><a href="#6i" class="faqitem">How is computing different from computer engineering (CE)?</a></li>
<li><a href="#7i" class="faqitem">What's the difference between all of the computing-related majors that Calvin offers?</a></li>
<li><a href="#8i" class="faqitem">Does Calvin have a program in video game design and development?</a></li>
<li><a href="#9i" class="faqitem">What kind of background do I need to study computing?</a></li>
<li><a href="#10i" class="faqitem">Are there any scholarships for computing students?</a></li>
<li><a href="#11i" class="faqitem">What is Calvin's policy regarding the Computer Science Advanced Placement (AP) tests?</a></li>
<li><a href="#12i" class="faqitem">How can I learn more?</a></li>
</ul>

<h2>Questions and Answers</h2>

<h4><a name="0i"></a>What is computing?</h4>
<div class="faqanswer">Computing (also known as computer science) is the study of all things related to <em>computation</em> or automated problem-solving, including: 

<ul>
<li>What computers can do and what they cannot do.</li>
<li>Ways that a person can instruct a computer to perform a
computation.</li>
<li>How information is described and manipulated.</li>
<li>Ways that people and computers interact.</li>
<li>Algorithms or "recipes" for specific computations and the
properties of those algorithms.</li>
<li>Strategies, techniques, and methodologies for designing a
computation.</li>
<li>The machines that perform computations.</li></ul>

<p>Computing is the off-spring of two very different
disciplines:</p>
<ul>
<li><em>Mathematics</em>, particularly the study of mathematical
models of computation; and</li>
<li><em>Electrical Engineering</em>, particularly the construction
of machines to perform computation.</li>
</ul>

<p>With these roots, computing is a
broad discipline whose areas range from the architectures of
specific machines to algorithms to programming languages to formal
models of computation. Put differently, computing is the
study of the <em>laws and principles that underlie
computation</em>.</p></div>
<a href="#topi" class="inlinenav">Back to the top</a><hr/>

<h4><a name="1ai"></a>Aren't the computing jobs all going to India?</h4>
<div class="faqanswer"><p>Absolutely not! 
In fact, the U.S. Bureau of Labor Statistics predicts that there will twice as many new U.S. jobs in software engineering as in the rest of engineering combined!  See our
<a href="http://cs.calvin.edu/p/ComputingCareersMarket">Market For Computing Careers
page</a> for charts showing the employment opportunities in computing.</p></div>
<a href="#topi" class="inlinenav">Back to the top</a><hr/>

<h4><a name="1"i></a>Doesn't computing just focus on programming?</h4>
<div class="faqanswer">Programming---instructing a computer to
perform a computation---is an important part of computing,
but it is just <em>one</em> of many areas of computing. Some of the
other areas include: 

<ul>
<li>algorithms</li>
<li>artificial intelligence</li>
<li>computer architecture</li>
<li>computer security</li>
<li>database systems</li>
<li>graphics</li>
<li>information systems</li>
<li>networks</li>
<li>operating systems</li>
<li>programming language design</li>
<li>software engineering</li>
<li>theory of computing</li></ul>
<p>The Calvin College Department of Computer Science offers courses in
each of these areas (and more).</p></div>
<a href="#topi" class="inlinenav">Back to the top</a><hr/>


<h4><a name="2i"></a>What kinds of jobs are there for people with computing degrees?</h4>

<div class="faqanswer"><p>For a person with a bachelors degree in computer science or information systems, there is a rich assortment of job opportunities. 
Recent graduates of Calvin's Department of Computer Science have taken jobs in:</p>

    <ul>
    <li>network engineering</li>
    <li>systems and website administration</li>
    <li>software design and development</li>
    <li>systems analysis</li>
        <li>computer education and support</li>
    </ul>


    <p>Also, a number of Calvin graduates have gone on to study at excellent graduate schools, including Michigan, MIT, Purdue Stanford, Texas, and Wisconsin.</p>

    <p>News media have reported that the market for computing-related jobs has cooled off, which has led many prospective students away from computing as a major in college.  This is unfortunate because according to the <a href="http://www.bls.gov/">Bureau of Labor Statistics</a>, there are more computing-related jobs today than there were in 1999 (at the height of the dot-com boom) and this is likely to remain true for the foreseeable future. </p>
<p>
We are experiencing this first-hand: each month, companies send our department
<a href="http://www.calvin.edu/archive/abstraction-jobs/">job and internship requests</a> -- far more requests than we have students!</p>
<p> 
A <a href="http://www.acm.org/globalizationreport/">recent study</a> by the <a href="http://www.acm.org/">Association for Computing Machinery (ACM)</a> indicates that "despite offshoring, career opportunities in IT will remain strong in the countries where they have been strong".  It notes that the most valuable people will be those who have a "strong foundational education", the ability to learn on their own, and the ability to do research.  These are things that Calvin focuses on in its CS and IS programs.
</p></div>
<a href="#topi" class="inlinenav">Back to the top</a><hr/>

<h4><a name="3i"></a>Won't I end up working at a computer in a cubicle the rest of my life (like Dilbert)?</h4>
<div class="faqanswer"><p>As we pointed out in an earlier question,
computer programming is just one of many different areas in
computing. There are lots of jobs related to computing
technology---ranging from sales to management to support to
education and training---that are highly people-oriented and
require strong communication skills.</p>
<p>In fact, many employers have told us that communication skills
and the ability to work in teams are the first things they look for
in a new computing employee. The clear implication is that
computing professionals today spend much of their time interacting
with people, not just machines.</p>
<p>Finally, there are many unfilled jobs in today's technology
sector so no one is going to force you to stay in a lousy job. If
you start in a job and find that you don't like it, keep your
skills up to date and there will be any number of other companies
who will welcome you with open arms. In today's market, computing
employees have lots of options!</p>
<p>Don't let the Dilbert stereotype scare you away from one of the
most rewarding careers imaginable!</p></div>
<a href="#topi" class="inlinenav">Back to the top</a><hr/>


<h4><a name="4i"></a>Does Calvin have a good computing program?</h4>
<div class="faqanswer"><p>The short answer is that Calvin has <strong>excellent</strong> programs in computing.</p>
    
    <p>The long answer is that the focus of the Department of Computer Science is the education of <em>undergraduate</em> computing professionals. We are a baccalaureate college, meaning that we only offer bachelors degrees, not masters or doctoral degrees. If you study computing at Calvin, each of your courses will be taught by a professor whose main interest is <em>teaching computing</em>, not a graduate student or professor whose primary interest is research and for whom teaching is strictly secondary.</p>

<p>Since this is the case at many baccalaureate colleges, how does Calvin compare to similar institutions?  Like many other departments across the US, we require all CS seniors to take the 
<a href="http://www.ets.org/">Educational Testing Service</a>'s 
<em>Computer Science Major Field Test</em> each year.
<a href="http://cs.calvin.edu/p/MFT_Results">
The past several years</a>, 
Calvin's institutional averages were above the 95th percentile -- our "average" students beat the average scores at 95% of the colleges and universities nationwide, so by this measure, Calvin's computer science program is in the top 5% in the U.S.

<p>National Science Foundation (NSF) data shows this is no fluke.
In its last comprehensive study <a href="http://www.nsf.gov/statistics/nsf96334/">Undergraduate Origins of Recent (1991-95) Science and Engineering Doctorate Recipients</a>, the NSF found that during the period of the study, nine Calvin College graduates completed PhDs in computer science. 
Using this measure, Calvin College is ranked #1 among baccalaureate colleges. Even more interesting, by this measure Calvin is tied with the #1 masters-granting university. Only twenty-three PhD-granting institutions produced more computer science PhDs over the years 1986-1995. (And each of the other institutions is many times larger than Calvin.)</p>

<p>What also sets our Computer Science department apart is that our <a href="/p/bcs">Bachelor of Computer Science degree</a> has been accredited by the Computing Accreditation Commission of the <a href="http://www.abet.org/">Accreditation Board for Engineering and Technology</a>.  While this is especially good for any student who wants to challenge taking all of the extra mathematics and science courses the <a href="/p/bcs">BCS</a> requires; it also benefits <em>all</em> of our degrees because all of our courses have to be up to the standards set by ABET.</p>

<p>Quite simply, you&rsquo;ll have a hard time finding a better undergraduate computer science education anywhere, particularly at a Christian college.</p>

<p>The strengths of our program include:</p>
    <ul>
        <li>Our <a href="/personnel/faculty">faculty</a>. Many of our faculty are recognized around the world for their expertise in different areas.</li>
        
        <li>Our <a href="/p/academics">academics</a>. By blending the study of the principles that govern computing with practical training, our curriculum prepares our students to succeed as computing professionals in the worlds of today and tomorrow. Our students study modern programming languages like C++, Java, Ada, and Smalltalk, and learn to use industrial strength platforms like Linux, Solaris (Sun's Unix), and Oracle.</li>
        
        <li>Our <a href="/p/facilities">environment</a>. Our computing laboratories and <a href="http://www.calvin.edu/library/">library facilities</a> combine to create a rich environment for learning about computing.</li>

        
        <li>Our <a href="/p/students">students</a>. Our computer science club <a href="http://clubs.calvin.edu/abstract/">Abstraction</a> and <a href="http://csx.calvin.edu/">CSX</a> help our department maintain a rich learning environment.</li>
        
        <li>Our <a href="/p/about_us">mission</a>. It is our calling to use our technical gifts and abilities to serve Jesus Christ, and we seek students who are similarly called.</li>
    </ul>

    <p>Calvin alumni have an amazing record of accomplishment.  Some have gone on to graduate study at distinguished universities like Stanford, MIT, Texas, Wisconsin, Illinois, Michigan, Michigan State, Indiana, Purdue, Utah, and Waterloo, and are now administrators or professors at major universities. Others have taken positions of responsibility at companies like Google, Microsoft, IBM, Cisco, Oracle, Boeing, and Ford Motor Co. Others serve at smaller companies.  Companies who hire our graduates value them for their work ethic and integrity.</p>
    
    <p>Come and join our tradition of excellence in computing at Calvin College!</p></div>
<a href="#topi" class="inlinenav">Back to the top</a><hr/>

<h4><a name="5i"></a>I'm interested in computing; what can I do to get started?</h4>
<div class="faqanswer"><p>While programming is not the only thing computing professional do, it is a good starting point.  Programming is best learned by writing programs.  If you can take a programming course at your high school or a local college, do so.  A reputable course would cover object-oriented programming with a main-stream language like Java, C++ or VB.Net.  It's possible that taking such a course could get you out of Calvin's introductory CS 108 course and into a more advanced course.  Talk to us at advising time if you have questions about this.</p>

  <p>If you can't find a programming course, you can always wait until fall and take <a href="/courses/cs/108/">CS 108</a>, Calvin's introduction to computing course.  CS 108 doesn't assume any prior programming experience.  However, if you'd like to get at least some programming experience before tackling CS 108, then you can play around at bit with Java programming.  Sun Microsystems provides a good Java development environment and <a href="http://java.sun.com/docs/books/tutorial/index.html">a Java programming tutorial</a>.</p>

  <p>The materials are all free and they work for Windows, Linux or Mac.  You can go through them as far as you'd like knowing that what you learn will give you something of a head start on CS 108.</p></div>
<a href="#topi" class="inlinenav">Back to the top</a><hr/>

<h4><a name="6i"></a>How is computing different from computer engineering (CE)?</h4>
<div class="faqanswer"><p>Computer engineers tend to focus on the
<em>hardware</em> aspects of computing---those "below" a
computer's operating system, including digital logic, circuits and
gates, building the physical devices to perform or support
computation, and so on.</p> 

<p>Computer scientists tend to focus on <em>software</em> aspects of computing -- the skills, concepts, techniques, and theories used to build computing systems, from the software applications a person runs to the operating system.</p>

<p>Computer scientists learn just enough about hardware to design software intelligently;
computer engineers learn just enough about software to design hardware intelligently.</p>

<p>
To make this a bit more concrete, consider a tablet computer like the iPad.
The tablet that you hold in your hand was mostly likely designed by computer engineers.
The operating system (iOS) and the multitude of apps that you can download from the App Store
were most likely designed by computer scientists.</p>

<p>Calvin provides programs in both of these areas.</p></div>
<a href="#topi" class="inlinenav">Back to the top</a><hr/>

    <h4><a name="7i"></a>What's the difference between all of the computing-related majors that Calvin offers?</h4>

    <p>The department offers programs in the following computing-related areas:</p>

<ul>
<li>The <a href="/p/bcs">BCS</a> is for students who want to
    challenge themselves with our strongest program in computing, mathematics and science.</li>
<li>The traditional <a href="/p/cs">BA in Computer Science</a> is for
    students who want a broader education, perhaps with a second major in some other area of interest.</li>
<li>The <a href="/p/is">BA in information Systems (IS)</a> is for students who want
    to focus on applying technology to the business environment; it's a
    great blend for someone choosing between computer technology and
    business management.  Our IS majors have go on to diverse careers as systems analysts, technology support specialists and software developers for business applications. </li>
<li>The <a href="/p/dc">BA in Digital Communications</a> is for
    students who are interested in applying computer technology to
    mass media; students take a lot of administration courses from us
    and several courses from CAS.</li>
</ul>
<p>You can find more information on these programs at our <a href="/p/academics">academics page</a>.</p>

    <a href="#topi" class="inlinenav">Back to the top</a><hr/>


<h4><a name="8i"></a>Does Calvin have a program in video game design and development?</h4>
<div class="faqanswer"><p>Video game design and development is a multi-disciplinary field that includes work in computing, mathematics, graphic arts, theater and management.  Calvin doesn't offer a specific "major" in this area, but rather allows you to major in Computer Science, Mathematics, Art, Theater or some related area, and then to collect a set of relevant supporting courses from the other areas.  Relevant courses at Calvin would include programming, computer graphics, acting, discrete mathematics, communication design, and video production.</p>

    <p>While we're pleased that so many people have become interested in computing through computer games, we hope that computing students don't narrow their focus too soon.  There's a whole range of computing-related vocations out there to be discovered.  God might use you mightily in the field of computer game design.  Alternatively, God might show you another path into one of the high-growth areas of computing, such as enterprise software design and development, network and security administration, and information systems.</p>

    <p>We believe that you would do well to find a school that provides you with the broad training you'll need in the long run as opposed to the more narrow courses you want at the moment.  This idea is central to Calvin's approach to education in computing.</p></div>
<a href="#topi" class="inlinenav">Back to the top</a><hr/>

<h4><a name="9i"></a>What kind of background do I need to study computing?</h4>

<div class="faqanswer"><p>Students who study computing at
Calvin arrive with a wide diversity of backgrounds. On average,
students with previous programming experience seem to have an
easier time in the first course (CS 108), but some of our best
students have been those with no previous programming experience.
So prior programming experience may be useful, but it is not
essential.</p>
<p>Many of our best students have taken as much high school
mathematics as possible, because computer science and mathematics
each require the same kind of rigorous thinking. That said, a
recent study found that the SAT verbal score was a better predictor
for success in computer science than the SAT quantitative
score.</p>
<p>Our best students are those who like to solve puzzles, because
the same patience and analytical ability that helps a person figure
out a puzzle helps a person figure out how to automate the solution
to a problem.</p>
<p>The main personal qualities that seem to make for a good
computing professional are</p>
<ul>
<li>creativity, because there are few limitations beyond one's
imagination when it comes to writing software applications;</li>
<li>love of learning, because computing technology changes so
rapidly, a computer scientist will be learning the rest of his or
her life;</li>
<li>attention to detail, because a computer will only do what you
tell it to do, not what you want it to do; and</li>
<li>perseverance, because as in other fields, success in computing
is 90% perspiration and 10% inspiration.</li></ul>

If you have these qualities, come and study computing at
Calvin!</div>
<a href="#top" class="inlinenav">Back to the top</a><hr/>

<h4><a name="10i"></a>Are there any scholarships for computing students?</h4>

    <p>The Computer Science Department offers computing-related
    scholarships, descriptions of which can be found at the <a href="/p/scholarships_and_awards">scholarships and awards page</a>.  Applications for these scholarships are solicited by the
      department during the spring semester.</p>
      
      <p>In addition, Calvin offers 
<a href="http://www.calvin.edu/admin/finaid/index.htm">scholarships and financial aid for all students</a>.</p>

<a href="#topi" class="inlinenav">Back to the top</a><hr/>

<h4><a name="11i"></a>What is Calvin's policy regarding the Computer Science Advanced Placement (AP) tests?</h4>
<div class="faqanswer"><p>Students taking the Computer Science
Advanced Placement Tests are exempted at Calvin College from the
following courses, based on your score:</p>
<table cellpadding="10" border="1">
<tr>
<th>Score</th>
<th>Computer Science A</th>
<th>Computer Science AB</th></tr>
<tr>

<td>1,2</td>
<td>none</td>
<td>none</td></tr>
<tr>
<td>3</td>
<td>none</td>
<td>CS 108</td></tr>
<tr>
<td>4, 5</td>
<td>CS 108</td>

<td>CS 108 &amp; CS 112</td></tr></table></div>

<a href="#topi" class="inlinenav">Back to the top</a><hr/>


<h4><a name="12i"></a>How can I learn more?</h4>
<div class="faqanswer">Come for a visit! 
<p>Calvin's <a href="http://www.calvin.edu/admin/admissions/">Admissions</a> department
hosts <a href="http://www.calvin.edu/admin/admissions/visit.htm">Fridays at
Calvin</a> visitation days most Fridays during the academic year.
You may <a href="http://www.calvin.edu/admin/admissions/facreg.htm">register
on-line</a>, or call 1-800-688-0122.</p>

<p>If you are unable to visit but would like more information about
Calvin College in general, please fill out an <a href="http://www.calvin.edu/admin/admissions/info.htm">on-line
information request form</a> and our Admissions staff will mail you
the information. Or take the <a href="http://www.calvin.edu/art/movies/qtvr98.htm">virtual tour of the
campus</a>.</p>
<p>If you
have specific questions about Calvin's Department of Computer
Science, feel free to <a href="/p/contact_us">contact us</a>.</p></div>
<a href="#topi" class="inlinenav">Back to the top</a><hr/>
      ''',
      'contentTab2Title': 'Current Students',
      'contentTab2': '''   <a name="topc"></a><h2>Questions</h2><ul class="faqlist">
      <li><a href="#0c" class="faqitem">What courses should I take?</a></li>
      <li><a href="#1c" class="faqitem">I want to get a job out of college; what will prepare me best for this?</a></li>
      <li><a href="#1.5c" class="faqitem">I'm thinking about going on to graduate school for further study; what are my options, and what should I be doing now to prepare?</a></li>
      <li><a href="#2c" class="faqitem">I want to go to graduate school for a Masters; what will prepare me best for this?</a></li>
      <li><a href="#3c" class="faqitem">I want to go to graduate school for a PhD; what will prepare me best for this?</a></li>
      <li><a href="#4c" class="faqitem">I want to do research in a particular area; what will prepare me best for this?</a></li>
      <li><a href="#5c" class="faqitem">I'm going for a BCS.  How can I satisfy the science course requirements?</a></li>
      <li><a href="#6c" class="faqitem">I would like to get a Business minor in addition to my Information Systems major.</a></li>
      <li><a href="#7c" class="faqitem">Can I install course software on my own computer?</a></li>
    </ul>

    <h2>Questions and Answers</h2>

    <h4><a name="0c"></a>What courses should I take?</h4> 

    <p>Start by studying the <a href="/p/academics">academics page</a>, which has links for
    each major program; those pages include sample schedules which
    take into consideration prerequisites and semester-by-semester
    course offerings.  Also look at the <a href="/p/schedule">schedule of all our courses</a>; some of our courses are offered in
    alternating years.</p>

    <p>With that basic background, talk to your faculty advisor.  He or she will be able to answer questions you may have, and will then help you craft a program that's right for you.</p>

    <a href="#topc" class="inlinenav">Back to the top</a><hr/>


    <h4><a name="1c"></a>I want to get a job out of college; what will
    prepare me best for this?</h4> 

    <p>Get a job while in college, either on your own or through our <a href="/courses/cs/394">internship program</a>.  Employers tend to look for potential employees who have demonstrated the ability to apply what they've learned in a real setting.  Also, get involved in extra-curricular activities, both computational and otherwise.  </p>

    <a href="#topc" class="inlinenav">Back to the top</a><hr/>

    <h4><a name="1.5c"></a>I'm thinking about going on graduate school for further study; what are my options, and what should I be doing now to prepare?</h4> 

    <p>Please see our <a href="/documents/graduate_school">Thinking About Graduate School?</a> page, as it has lots of grad-school related advice.  
       Then talk to your advisor and/or other CS faculty members to get their advice.</p>

    <a href="#topc" class="inlinenav">Back to the top</a><hr/>

    <h4><a name="2c"></a>I want to go to graduate school for a Masters;
    what will prepare me best for this?</h4> 

    <p>Apply.  And get involved in a lot of extra
    curricular activities.  Do the same things that an undergraduate
    planning on a PhD would do.</p> 

    <a href="#topc" class="inlinenav">Back to the top</a><hr/>


    <h4><a name="3c"></a>I want to go to graduate school for a PhD; what will prepare me best for this?</h4>

    <p>First you have to really consider <em>why</em> you want a PhD.
    If your goal is research (academic or industrial) or college
    teaching, then you'll need a PhD; otherwise, you probably don't
    need one.  Even some industrial research positions will accept
    just a Masters.</p>
      
    <p>If you decide you really do want a PhD, take the hardest
    classes in Computer Science and take a hard minor.  The 
<a href="/p/bcs">BCS</a> is certainly good; if you opt for the 
<a href="/p/cs">BA in CS</a>, you should have a hard minor or a
    second major.  It used to be the case that graduates schools
    <em>preferred</em> a BA; it indicates a breadth of knowledge and
    an ability to learn without being spoon-fed the material.  While
    this may still be true in other disciplines and while a BA won't
    <em>hurt</em> your chances, the BCS is certainly highly
    regarded.</p>

    <p>You need to do well in your classes, especially the upper-level
    electives.  You need a a good score on the GRE, the general exam
    in particular.  Not all graduate programs require a subject test,
    and generally that's one of the <em>last</em> things that an
    admissions committee will consider.</p>
      
    <p>Get involved in <em>lots</em> of extra curricular
    activities.</p>
      
    <p>If at all possible, get involved in some research here at
    Calvin or elsewhere during the summer; a published paper while an
    undergraduate opens <em>lots</em> of doors!</p>

    <a href="#topc" class="inlinenav">Back to the top</a><hr/>

    <h4><a name="4c"></a>I want to do research in a particular area;
    what will prepare me best for this?</h4>

    <p>Generally, the answer is "take more math".  Computer graphics
    requires math; neural networks requires math; compilers requires
    math.  They don't all need the same types of math, so you have to
    choose those courses somewhat wisely (with the help of your
    advisor), but math is going to be probably your best bet.  If your
    research is in a particular science (e.g., bioinformatics), then
    you'll want to take courses in that area.</p>

    <p><a href="#topc" class="inlinenav">Back to the top</a><hr/></p>

    <h4><a name="5c"></a>I'm going for a BCS.  How can I satisfy the
      science course requirements?</h4> 

    <p>A few things to note:</p>
    <ul>
      <li> A high school exemption for a core requirement does
    <em>not</em> count toward a BCS. </li> 
      <li> AP credit <em>does</em> count for the BCS if the
    corresponding department accepts it as an exemption for the
    right course.  For example, AP Chemistry counts toward a BCS
    if and only if the Chemistry department exempts you from CHEM
    103 or CHEM 104. </li> 

      <li> PHYS 133-135, PHYS 133-235, and CHEM 103-104 count
    toward the two-course sequence for a BCS <em>and</em> they
    satisfy <em>both</em> core requirements (physical and living
    world).  This leaves you open to take <em>any</em> approved
    course from <em>any</em> other department.  (In the past, BCS
    students were effectively required to take BIOL 141 for the
    BCS and to satisfy core; the new core requirements of 2004
    give you more options.) </li> 

    </ul>

    <a href="#topc" class="inlinenav">Back to the top</a><hr/>

    <h4><a name="6c"></a>I would like to get a Business minor in
    addition to my Information Systems major.</h4>

    <p>This is a popular choice since you've already taken many of the
    courses in the Business minor; however, there is a small problem
    because of that overlap: you are allowed only a <em>two</em>
    course overlap between your major and minor.  The Business minor
    and IS major overlap in <em>three</em> courses (BUS 160, BUS 203,
    and ECON 221).  You can easily solve this problem by taking one
    more BUS or ECON elective which will substitute for one of these
    three in the major.  For example, many students take BUS 204 to
    satisfy the IS major instead of BUS 203; they take BUS 203 to
    satisfy the minor.  Discuss your options with your advisor.</p>

    <a href="#topc" class="inlinenav">Back to the top</a><hr/>   

    <h4><a name="7c"></a>Can I install course software on my own computer?</h4>

    <p>Generally speaking, yes.  Most Unix-based software is open source (e.g., Linux, Java, C++, Eclipse) and most Microsoft software can be downloaded through our <a href="http://cs.calvin.edu/p/msdnaa">MSDNAA program</a>.</p> 
    
    <a href="#topc" class="inlinenav">Back to the top</a><hr/>

      ''',
      'date': datetime.strptime('2014-9-1', '%Y-%m-%d')
      },
     
     {'name': 'software', 
      'ordinal': 3,
      'title': 'Software and Services',
      'summary': 'Software applications and services',      
      'content': '''<p>The department maintains a variety of sources for software and software services.</p>
<ul>
<li><a href="http://e5.onthehub.com/WebStore/ProductsByMajorVersionList.aspx?ws=c67f6f25-c79b-e011-969d-0030487d8897&vsro=8&JSEnabled=1">Microsoft Dreamspark</a> &mdash; The Departments of Computer Science and Engineering have joined Microsoft&rsquo;s <a href="https://www.dreamspark.com/">Dreamspark Program.</a>.
Students in CS or ENGR courses can use it to get software for their own personal, academic use. </li>
<li><a href="http://mirror.calvin.edu">Software Mirror</a> &mdash; <a href="http://abstract.calvin.edu">Abstraction</a> maintains a software mirror. </li>
<li><a href="http://abs.calvin.edu">Abs</a> &mdash; <a href="http://abstract.calvin.edu">Abstraction</a> also maintains a set of software services. </li>
</ul>
<p>For more information on these resources, contact <a href="mailto:computing@calvin.edu">computing@calvin.edu</a> or
<a href="mailto:abstraction@calvin.edu">abstraction@calvin.edu</a>.</p>
''',
         'date': datetime.strptime('2014-9-1', '%Y-%m-%d')
    },
     {'name': 'scholarships',
      'ordinal': 2,
      'title': 'Scholarships',
      'summary': 'Information on scholarships and awards for current and incoming students',
      },         
     {'name': 'facilities', 
      'ordinal': 4,
      'title': 'Facilities',
      'summary': 'Special-purpose computer labs',
      'content': '''<p>The department maintains a variety of facilities for course work and research.</p>
      <h3>Class-Lab Facilities</h3>
<ul>
<li><strong>GLUW Lab</strong>: a 34-seat facility of custom multi-boot (Linux, Windows) workstations.</li>
<li><strong>Hardware Lab</strong>: a lab for assembling and/or diagnosing computer hardware.</li>
<li><strong>Systems Lab</strong>: Systems Lab, a 24-seat specialized lab for OS, networking, and security work.</li>
<li><strong>Windows Lab</strong>: Windows Lab, a 34-seat facility for computer literacy courses.</li>
</ul>
      <h3>Research Facilities</h3>
<ul>
<li><strong>CSX Lab</strong> (SB 319): This lab is maintained by the <a href="http://abstract.calvin.edu">Abstraction</a> student club.</li>
<li><strong>Supercomputing Lab</strong>: This lab is the home of the department&rsquo;s beowulf clusters.</li>
<li><strong>CCEL Lab</strong>: This lab is the &ldquo;brick and mortar&rdquo; division of the <a href="http://www.ccel.org">Christian Classics Etherial Library</a>.</li>
</ul>
<p>For more information on these facilities, contact <a href="mailto:computing@calvin.edu">computing@calvin.edu</a>.</p>
''',
         'date': datetime.strptime('2014-9-1', '%Y-%m-%d')
    },
     
     {'name': 'club',
      'ordinal': 6,      
      'title': 'Student Club',
      'summary': 'The Calvin club for computing students: <a href="http://clubs.calvin.edu/abstract" class="external">Abstraction</a>',
      'date': datetime.strptime('2014-9-1', '%Y-%m-%d')
      },
     
     {'name': 'listservs',
      'ordinal': 7,
      'title': 'Mailing Lists',
      'summary': 'Abstraction&rsquo;s collection of useful <a href="http://clubs.calvin.edu/abstract/mailing-lists/" class="external">mailing lists</a>',
      'date': datetime.strptime('2014-9-1', '%Y-%m-%d')
      },
     
     {'name': 'jobs',
      'ordinal': 5,
      'title': 'Job Opportunities',
      'summary': 'A list of job opportunities for either internships or full-time work',
      'content': '''
      <p>Here are a number of sources for job opportunities.<p>
      <ul>
<li><a href="http://www.calvin.edu/archive/abstraction-jobs/" class="external">Abstraction&rsquo;s job list</a>: 
Abstraction maintains an archive of all job advertisements the department receives. Subscribe to abstraction-jobs to receive these 
emails directly.</li>
<li><a href="https://calvin-csm.symplicity.com/students/" class="external">CalvinLink</a>: Calvin&rsquo;s Career Services maintains CalvinLink, a list of job opportunities.</li> 
</ul>
      <p>The market for computing professionals is strong, see the department&rsquo;s <a href="/documents/careers">Market for Computing Careers</a>.<p>
      ''',
      'date': datetime.strptime('2014-9-1', '%Y-%m-%d')
      },
     
     {'name': 'calvin_student_resources',
      'ordinal': 8,
      'title': 'Calvin Student Resources',
      'summary': 'Calvin&rsquo;s resources for all students: <a href="http://www.calvin.edu/students" class="external">Students</a>',
      'date': datetime.strptime('2014-9-1', '%Y-%m-%d')
      }
     
     ],
    
    # departments...
    [{'name': 'cs',
      'title': 'Computer Science',
      'tagline': 'Creating Tomorrow&rsquo;s Technology Today',
      'shortDescription': '''<p>Calvin&rsquo;s <a href="http://www.abet.org/" alt="ABET organization">ABET</a>-accredited Bachelor of Computer Science degree and related degrees in information systems and digital media are taught from a <a href="/documents/christian_computing" alt="christian computing resources">Christian perspective</a> and give you the opportunity to be <em>creative</em>, to <em>make a difference</em> and to pursue a <a href="/documents/computing_careers"><em>great career</em></a>.</p>
        <p>
            <iframe src="http://player.vimeo.com/video/23780397?title=0&amp;byline=0&amp;portrait=0" width="300" height="175" frameborder="0"></iframe> &nbsp;
           <iframe src="http://player.vimeo.com/video/24137603?title=0&amp;byline=0&amp;portrait=0" width="300" height="175" frameborder="0"></iframe>
            <br>
            <a href="http://vimeo.com/calvincomputerscience/">see more computing videos...</a>
        </p>''',
          'longDescription': '''<p>
            Welcome! We&rsquo;re passionate about undergraduate education in computing that is both <em>academically
                excellent</em> and <em>distinctively Christian</em>. Since we began offering computing courses in 1968, we have worked
            hard to achieve both of these goals without compromise.
        </p> 
        
        <h2>Our Programs</h2>
        <div style="float: right; padding: 10px"><img src="/static/images/CAC-RGB-W-S.png" border="1px"></div>
        <p>
            Our <a href="/p/bcs"><span class="caps">BCS</span></a> program is <a href="/p/accreditation">accredited</a> by <a
                href="http://www.abet.org/"><span class="caps">ABET</span></a>, a distinction we share with select programs around
            the country (e.g., <span class="caps">MIT</span> and Michigan), and we&#8217;ve leveraged the <span class="caps">BCS</span>
            courses to build specialized programs in information systems, digital communication and digital art (see our <a
                href="/p/academics">academics page</a>).
        </p>
        <p>
            In addition to taking courses, our students apply their skills in a number of venues, including paid internships,
            design projects and community outreach programs. In so doing, they learn how their education can become the basis of
            a life-long vocation of service (see our <a href="/mission">mission statement</a> and our <a
                href="/p/christian_scholarship">essays on Christian scholarship</a>).
        </p>
        <h2>Our Students</h2>
        
<p>Our graduates do well in both graduate schools and business. They&rsquo;ve been accepted and/or employed at a variety of places, including the following.</p>
<table class="scrollable" style="height: 150px">
  <tr>
  <th>Graduate programs:</th>
  <th>International Companies &amp; Organizations:</th>
  <th>West Michigan Companies &amp; Organizations:</th>
  </tr>
  <tr>
  <td>
    <ul>
      <li>MIT</li>
      <li>Harvard</li>
      <li>Berkeley</li>
      <li>Stanford</li>
      <li>Purdue</li>
      <li>Michigan</li>
      <li>Michigan State</li>
      <li>Ohio State</li>
      <li>Illinois, Urbana-Champaign</li>
      <li>Wisconsin</li>
      <li>Texas</li>
      <li>USC</li>
    </ul>
  </td>
  <td>
    <ul>
      <li>Google</li>
      <li>Microsoft</li>
      <li>Facebook</li>
      <li>Yahoo</li>
      <li>IBM</li>
      <li>Boeing</li>
      <li>FBI</li>
      <li>Crowe Chizek</li>
      <li>Peace Corps</li>
      <li>Wycliffe Bible Translators</li>
    </ul>
  </td>
  <td>
    <ul>
      <li>Herman Miller</li>
      <li>Steelcase</li>
      <li>Meijer</li>
      <li>GFS</li>
      <li>OST</li>
      <li>Quixtar/Alticor</li>
      <li>Spectrum Health</li>
      <li>Atomic Object</li>
      <li>GE Aviation</li>
    </ul>
  </td>
  </tr>
</table>  

        <p>
            An <span class="caps">NSF</span> study showed that graduate programs awarded more PhDs in computer science to Calvin
            graduates <em>than to any other comparably sized school</em>.
        </p>        

         <p>
            Calvin CS students routinely do well on the <a
                href="http://www.ets.org/portal/site/ets/menuitem.1488512ecfd5b8849a77b13bc3921509/?vgnextoid=fd29af5e44df4010VgnVCM10000022f95190RCRD&vgnextchannel=86f346f1674f4010VgnVCM10000022f95190RCRD"><span
                class="caps">ETS</span></a> Major Field Test for Computer Science.</p>

<div id="etsChartWrapper" class="chartWrapper">
<h3>ETS Scores for Computer Science Graduates (most recent five years)</h3>
<div id="etsChart" class="chartContent" style="height: 250px; width: 90%;"></div>
<div id="etsLegend" class="chartLegend"></div>
<div id="etsFooter" class="chartFooter"></div>
</div>
<script>
// Numbers of students in the given percentiles per year (2012-present)
var mostRecentYearCount = 5;
var rawCounts = [
    ["0-9", [0,0,0,0,2]],
    ["10-19", [0,0,0,0,2]],
    ["20-29", [0,0,0,0,2]],
    ["30-39", [0,1,0,1,3]],
    ["40-49", [0,0,0,0,3]],
    ["50-59", [1,0,0,1,0]],
    ["60-69", [1,2,3,1,4]],
    ["70-79", [1,0,2,0,0]],
    ["80-89", [1,0,3,5,3]],
    ["90-99", [5,2,8,9,1]]
];
var labelledCountSums = rawCounts.map(function(row){
    return [ row[0], row[1].slice(-1 * mostRecentYearCount).reduce(function(sum,x){
        return sum+x;
    }) ];
});
var options = {
                series: {
                                bars: {
                                                show: true,
                                                barWidth: 0.66,
                                                align: "center"
                                }
                },
                colors: ["#550000"],
                xaxis: {
                                mode: "categories",
                                tickLength: 0,
                                axisLabel: "Percentiles",
                                axisLabelUseCanvas: true,
        axisLabelFontSizePixels: 12,
        axisLabelPadding: 5
                },
                yaxis: {
                                axisLabel: "Student Count",
                                axisLabelUseCanvas: true,
        axisLabelFontSizePixels: 12,
        axisLabelPadding: 5
                }
};
$.plot($("#etsChart"), [ labelledCountSums ], options);
$("#etsLegend").append("<center><small>Flot " + $.plot.version + "</small></center>");
</script>

<p>As can be seen here, our average students routinely score at or above the 90th percentile nation-wide.
Note that the scores include all senior CS majors, not just those from the BCS program.</p>

<p>The following charts show the total enrollment and graduates by major program.</p>

<div id="enrollmentChartWrapper" class="chartWrapper">
<h3>Total Number of Students by Major Program</h3>
<div id="enrollmentChart" class="chartContent" style="height: 250px; width: 90%;"></div>
<div id="enrollmentLegend" class="chartLegend"></div>
<div id="enrollmentFooter" class="chartFooter"></div>
</div>
<script>
var bcsRaw = [21, 26, 26, 38, 45, 27, 13, 9, 20, 11, 17, 22, 35];
var csRaw = [120, 92, 20, 45, 29, 37, 36, 38, 34, 42, 36, 57, 58];
var isRaw = [0, 3, 16, 28, 34, 26, 23, 26, 21, 20, 21, 21, 19];
var dcRaw = [0, 3, 3, 9, 14, 9, 8, 9, 6, 8, 6, 9, 13];
var bcs = [], cs = [], is = [], dc = [], total = [];
var year = 2002;
for (var i = 0; i < bcsRaw.length; i++) {
    bcs.push([year, bcsRaw[i]]);
    cs.push([year, csRaw[i]]);
    is.push([year, isRaw[i]]);
    dc.push([year, dcRaw[i]]);
    total.push([year, bcsRaw[i] + csRaw[i] + isRaw[i] + dcRaw[i]]);
    year++;
}
var data = [ 
        { label: "total", data: total },
        { label: "cs", data: cs },
        { label: "bcs", data: bcs }, 
        { label: "is", data: is },
        { label: "dc", data: dc }
        ]
var options = {
    series: { 
        lines: { show: true, fill: false },
        points: { show: false }
    },
    grid: {
        hoverable: true
    },
    legend: { 
        container: $("#enrollmentLegend"),
        noColumns: 1
    },
    colors: ['#AA5555','#88CC88','#8888CC','#CCCC88','#CC88CC']
}
$.plot("#enrollmentChart", data, options); 
$("#enrollmentLegend").append("<center><small>Flot " + $.plot.version + "</small></center>");  
</script>

<p>The IS and DC programs were started in 2002.</p>

<div id="graduatesChartWrapper" class="chartWrapper">
<h3>Number of Graduates by Major Program</h3>
<div id="graduatesChart" class="chartContent" style="height: 250px; width: 90%;"></div>
<div id="graduatesLegend" class="chartLegend"></div>
<div id="graduateFooter" class="chartFooter"></div>
</div>
<script>
var bcsRaw = [11, 8, 11, 8, 4, 11, 3, 3, 2, 6, 3, 2, 9];
var csRaw = [19, 15, 18, 6, 10, 8, 5, 6,6, 4, 1, 4, 8];
var isRaw = [0, 0, 1, 4, 14, 9, 7, 6, 7, 6, 4, 6, 7];
var dcRaw = [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0];
var bcs = [], cs = [], is = [], dc = [], total = [];
var year = 2002;
var yearString;
for (var i = 0; i < bcsRaw.length; i++) {
    bcs.push([year, bcsRaw[i]]);
    cs.push([year, csRaw[i]]);
    is.push([year, isRaw[i]]);
    dc.push([year, dcRaw[i]]);
    total.push([year, bcsRaw[i] + csRaw[i] + isRaw[i] + dcRaw[i]]);
    year++;
}
var data = [ 
        { label: "total", data: total },
        { label: "cs", data: cs },
        { label: "bcs", data: bcs }, 
        { label: "is", data: is },
        { label: "dc", data: dc }
    ]
var options = {
    series: { 
        lines: { show: true, fill: false } 
    },
    legend: { 
        container: $("#graduatesLegend"),
        noColumns: 1
    },
    colors: ['#AA5555','#88CC88','#8888CC','#CCCC88','#CC88CC']
}
$.plot("#graduatesChart", data, options);    
$("#graduatesLegend").append("<center><small>Flot " + $.plot.version + "</small></center>");  
</script>

<p>As you can see, our numbers reflect the (nationwide) drop in CS enrollments between 2002 and 2008, 
followed by rapid growth as the market began responding to the demand for computing professionals.</p>

<h2>Getting Started in Computing at Calvin</h2>

        <ul>
            <li>See our <a href="http://vimeo.com/calvincomputerscience/videos/sort:oldest"> department videos</a> on Vimeo
            </li>
            <li>See our <a href="faq_incoming" title="FAQ">frequently asked questions</a> for incoming students.
            </li>
            <li>Request more information by <a href="/contact">contacting us</a></li>
        </ul>
          ''',
       'contact': '''    <p><strong>Department of Computer Science</strong><br>
    North Hall | <a href="http://www.calvin.edu/map/index.htm?building=NH"
                    alt="North Hall map">map</a><br>
    Calvin College<br>
    Grand Rapids, MI 49546<br>
    USA<br>
    1-616-526-7163<br>
    computing@calvin.edu
    </p>
    ''',
    'research': '''
    <p>The department maintains a number of active research and scholarship programs, including the following.</p>
    <h3>Faculty Research</h3>
    <ul>
    <li><strong>Computational Science</strong> &mdash; Serita Nelesen actively participates in Calvin&rsquo;s <a href="http://www.calvin.edu/isri/">Integrated Science Research Institute</a>. Serita Nelesen, particular, conducts research in computational biology and bioinformatics.</li>
    <li><strong>Digital Libraries</strong> &mdash; Harry Plantinga built and maintains the <a href="http://www.ccel.org" alt="The CCEL Website">Christian Classics Ethereal Library</a>, 
    a digital library of well-known Christian literature, and <a href="http://www.hymnary.org">Hymnary.org</a>, a comprehensive 
    repository of Christian hymns, that are two of the most commonly visited Christian websites on the world-wide-web. 
    This work is funded by a variety of sources and employs a number of students throughout the year.</li>
    <li><strong>High-Performance Computing</strong> &mdash; Joel Adams designs and builds high performance Beowulf clusters (see <a href="http://dahl.calvin.edu/">Dahl</a> & <a href="http://www.calvin.edu/~adams/research/microwulf/">Microwulf</a>), 
    and applies their computational power to hard problems in the sciences. This work has been funded by the NSF, employs student interns, 
    and serves as the basis for the high-performance computing course (see <a href="/courses/cs/374" alt="CS 374 website">CS 374</a>).</li>
    </ul>
    <h3>Student Research</h3>
    <p>In addition to participating in faculty research projects (listed above), students run their own research 
    projects. One common place for this work is the senior projects course. For details, see <a href="/courses/cs/396">CS 396/398</a>.</p>
    <h3>Computing Outreach Programs</h3>
    <p>The department has established a number of programs dedicated to the introduction of computing to the general community, and, 
    in particular, to under-represented groups.</p>
    <ul>
    <li><strong>Computer Camps</strong> &mdash; Joel Adams runs computer camps, focusing on both
    <a href="http://alice.calvin.edu">Alice</a> and <a href="http://www.calvin.edu/pre-college/camps/academic/computer.html">Scratch</a>.</li>
    <li><strong>After-School Programs</strong> &mdash; Vic Norman runs <a href="http://www.tecreate.org/">TeCreate</a>, an 
    after-school program for secondary school students.</li>
    </ul>
    <h3>Computer Science Education</h3>
    <p>The department has written books and lab materials for courses using a variety of programmin environments.</p>
    <ul>
    <li><a href="/books/c++/">C++</a></li>
    <li><a href="/books/ds/">Data structures</a></li>
    <li><a href="/books/fortran/">Fortran</a></li>
    <li><a href="/books/java/">Java</a></li>
    <li><a href="/books/networking/">Networking</a></li>
    <li><a href="/books/processing/">Processing</a></li>
    </ul>
    <h3>Christian Scholarship in Computing</h3>
    <p>The department studies the Christian underpinnings of computing. For details, see the materials available at 
    <a href="/documents/christian_computing">Christianity and Computing</a>.</p>
    ''', 
    'honors': '''
     <p>Calvin challenges its best students by offering an <a href="http://www.calvin.edu/academic/honors/">honors program</a>.  This program nurtures collaboration between individual students and faculty on projects of mutual interest.  All of the degrees offered by the department can be taken for honors.</p>
<h3>Graduating with Honors in Computing</h3>

  <p>In addition to the 
<a href="http://www.calvin.edu/honors/details/graduating-with-honors.html">college-wide requirements</a>, the department adds these requirements:</p>

<ul>
    <li>An honors student must take at least two of their honors courses in their major (to complement the two courses outside their 
    major/department that are required by the campus-wide program).</li>
    <li>An honors program in computing must include <span class="caps">MATH</span> 171 (Calculus I), <span class="caps">MATH</span> 172 
    (Calculus II), and <span class="caps">MATH</span> 243 (Statistics), and at least four electives.  
    (n.b., <a href="/academics/bcs"><span class="caps">BCS</span></a> majors are already required to meet these requirements.)</li>
    <li>An honors student must propose an honors program (normally in their sophomore year).  This program is designed by the student and 
    the student&#8217;s mentor, and must be approved by the department.</li>
    <li>An honors student must complete a senior honors project, which must be significantly more challenging than a typical senior project. 
    This project must be presented in an appropriate public forum (e.g., a conference or department colloquium) and must be approved by the 
    department (see <a href="/courses/cs/396/">CS 396/398</a> for more details on the senior project with honors).</li>
</ul>

<h3>Honors Courses</h3>
<p>The Computer Science Department does not offer any special honors sections of its courses, but any course (at the discretion of the instructor) can be taken for <em>honors by contract</em>. Students who want more of a challenge from a course (even if they are not going to graduate with honors) are encouraged to take courses for honors by contract.</p>

<p>To take a course for honors by contract, students must request this from the professor within the first two weeks of the semester.  Granting these requests is up to the instructor for the course.  Courses commonly taken for honors include one introductory course (e.g., 
<a href="/courses/cs/108">CS 108</a>, 
<a href="/courses/cs/112">CS 112</a> and 
<a href="/courses/cs/212">CS 212</a>) and one advanced course of the student&#8217;s choice.  To request honors by contract, using the following form:</p>
<ul>
<li><a href="/department/honors/contract.html">Honors by Contract Form (<span class="caps">HTML</span>)</a></li>
</ul>''',
'courseSchedule': '''
  <h2>Annual Courses</h2>
<table border="1">
<tr>
  <th>Semester</th>
  <th>Computer Science</th>
  <th>Information Systems</th>
</tr>
<tr>
<td style="vertical-align: top;">Fall</td>
<td style="vertical-align: top;">
<ul>
<li>CS 100 (Web Media)</li>
<li>CS 104 (Applied C++)</li><li>CS 108/106 (Introduction to Computing)</li><li>CS 112 (Introduction to Data Structures)</li><li>CS 212 (Data Structures and Algorithms)</li><li>CS 262 (Software Engineering)</li><li>CS 195/295 (Seminar)</li><li>CS 394 (Internship)</li></ul>
</td>
<td style="vertical-align: top;">
<ul>
<li>IS 141 (Computing with Databases)</li><li>IS 171 (Computing with Spreadsheets)</li><li>IS 271 (Introduction to Information Systems)</li><li>IS 337 (Introduction to Website Administration)</li></ul>
</td>
<tr>
<td style="vertical-align: top;">Spring</td>
<td style="vertical-align: top;">
<ul>
<li>CS 108 (Introduction to Computing)</li><li>CS 112 (Introduction to Data Structures)</li><li>CS 214 (Programming Languages)</li><li>CS 232 (Operating Systems and Networking)</li><li>CS 195/295 (Seminar)</li><li>CS 384 (Perspectives)</li><li>CS 394 (Internship)</li></ul>
</td>
<td style="vertical-align: top;">
<ul>
<li>IS 141 (Computing with Databases)</li><li>IS 171 (Computing with Spreadsheets)</li><li>IS 333 (Network Administration)</li></ul>
</td>
</tr>
</table>
<h2>Alternate Year Courses</h2>
<table border="1">
<tr>
  <th>Semester</th>
  <th>Computer Science</th>
  <th>Information Systems</th>
</tr>
<tr>
  <td>Fall, Odd Years</td>
<td>
<ul>
 <li>CS 364 (Computer Security)</li>
<li>CS 374 (High Performance Computing)</li>
</ul>
</td>
<td>
<ul>
 <li>IS 341 (Database Administration)</li>
</ul>
</td>
</tr>
<tr>
  <td style="vertical-align: top;">Spring, Even Years</td>
<td>
<ul>
 <li>CS 300 (Bioinformatics)</li>
<li>CS 332 (Networking) or 320 (Advanced Computer Architecture)</li>
</ul>
</td>
  <td>&nbsp;</td>
</tr>
<tr>
  <td>Fall, Even Years</td>
<td>
<ul>
<li>CS 312 (Logic, Computability, and Complexity)</li>
<li>CS 344 (Artificial Intelligence)</li>
</ul>
</td>
  <td>&nbsp;</td>
</tr>
<tr>
  <td style="vertical-align: top;">Spring, Odd Years</td>
<td>
<ul>
   <li>CS 342 (Database Management Systems)</li>
   <li>CS 352 (Computer Graphics)</li>
</ul>
</td>
<td>
<ul>
<li>IS 371 (Information Systems Leadership)</li></ul>
</td>
</tr>
</table>
<h2>Interim Courses</h2>
<table border="1" cellpadding="10px">
<tr>
  <td style="vertical-align: top;">Interim 2015</td>
  <td><a href="/p/interim2015">CS W60 &#8211; Christian Computing: Thailand</a></td>
</tr>
</table>
'''
          }],

        # users...
        [
            {'name': 'calvin', 'password': custom_app_context.encrypt('h4bb2s')},
        ],

        # images...
        [{'name': 'micwic2011',
           'filename': 'micwic2011-1494x519px.jpg',
           'description': '''Calvin CS faculty and students attend the MICWIC Conference.''',
           'tags': ['departments.cs']},
          {'name': 'gluwlab',
           'filename': 'gluwlab-1494x519px.jpg',
           'description': '''CS and IS students get hands-on experience in Calvin&rsquo;s main computing lab.''',
           'tags': ['departments.cs']},
          {'name': 'lightsaber',
           'filename': 'lightsaber-1494x494px.jpg',
           'description': '''Jess Vriesema works on the physics of our VR <a href="http://www.calvin.edu/news/2006-07/jedi-trainer">Jedi Trainer</a>.''',
           'tags': ['departments.cs']}
          ],
        
        # scholarships...
        [{'name': 'vanderbrug',
          'ordinal': 3,
           'shortDescription': '''The VanderBrug scholarships are given to upper-division students in computer science.''',
#            'shortDesc': '''The Gordon J. VanderBrug scholarships are funded by an endowment graciously provided by the VanderBrug family. They are given to strong juniors and seniors in computer science. Interested Calvin students should apply in the Spring semester for the following year.''',
           'programs': ['bcs', 'cs', 'is'],
           'recipients': '''
<table class="scrollable" style="height: 300px">
            <tr><th>Year</th><th>Recipients</th></tr>
            <tr><td>2013/14</td><td>Patrick Hess & Ruth Holtrop</td></tr>
            <tr><td>2012/13</td><td>John Kloosterman & Ha Kyung Kong</td></tr>
            <tr><td>2011/12</td><td>John Kloosterman & Ha Kyung Kong</td></tr>
            <tr><td>2010/11</td><td>Nathan Brink, Nathaniel Burns & Aaron Etzler</td></tr>
            <tr><td>2009/10</td><td>Nathaniel Burns & Jonathan Roshko</td></tr>
            <tr><td>2008/09</td><td>Dan Brown, Allison Thompson, & Jon Walz</td></tr>
            <tr><td>2007/08</td><td>Dan Brown, Allison Thompson, & Jon Walz</td></tr>
            <tr><td>2006/07</td><td>Nathan Beach, Dan Brown, & Allison Thompson</td></tr>
            <tr><td>2005/06</td><td>Josh Holtrop</td></tr>
            </table>
            ''',
                 'appInfo': None
#                        'appInfo': '''To Apply: Use the Upper Class Named Scholarship Application Form on Calvin Portal: 
#              > Students 
#                > Scholarship and Financial Aid 
#                 > Upper Class Named Scholarship Application.'''
                },

         {'name': 'science',
          'ordinal': 7,
           'title': 'Science Division Scholarships',
           'shortDescription': '''The Calvin College Science Division provides a variety of scholarship opportunities.''',
           'details':None,
           'programs': ['bcs', 'cs', 'is'],
           'recipients':None,
           'appInfo':None,
           'url': 'http://www.calvin.edu/academic/science/scholarships/'},                  

              {'name': 'dornerworks',
          'ordinal': 4,               
           'shortDescription': '''The DornerWorks scholarship is awarded to a student who is interested in embedded systems.''',
#            'shortDesc': '''The DornerWorks Computer/Software Engineering Scholarship is funded by DornerWorks Ltd. The scholarship is given to a strong sophomore, junior, or senior majoring in computer engineering or computer science. Students must be full-time and have a 3.3 or higher GPA. Preference will be given to students who have an internship with DornerWorks, who are interested in embedded systems, who have demonstrated leadership ability, who have financial need, and/or are entering their junior year. Interested first, second, and third-year Calvin students should apply in the Spring semester for the following year. ''',
           'details': '''DornerWorks Ltd is an electronics engineering consulting firm founded in 2000 by David Dorner, located in Grand Rapids, MI. The company offers its clients consulting expertise in electronic hardware, embedded software, and custom logic design, especially avionics and medical devices. We gratefully thank Mr. Dorner for his generosity in funding this scholarship. ''',
           'programs': ['bcs', 'cs', 'is'],
           'recipients': '''
<table class="scrollable" style="height: 300px">
<tr><th>Year</th><th>Recipients</th></tr>
<tr><td>2013/14</td><td>Cheyne Rushing</td></tr>
<tr><td>2012/13</td><td>John Kloosterman</td></tr>
<tr><td>2011/12</td><td>Daniel Ziegler</td></tr>
<tr><td>2010/11</td><td>Nathan Brink</td></tr>
<tr><td>2009/10</td><td>Avery Sterk</td></tr></table>''',
            'appInfo': None
#            'appInfo': '''To Apply: Use the Upper Class Named Scholarship Application Form on Calvin Portal:
#  > Students
#    > Scholarship and Financial Aid
#     > Upper Class Named Scholarship Application.'''
    },


        {'name': 'derose',
                   'ordinal': 1,
           'shortDescription': '''The DeRose scholarship is given to a strong first year computer science major, and it normally continues through their second year.''',
#            'shortDesc': ''' ''',
           'details': '''Dr. DeRose is a world-class expert on technologies for electronic documents, including markup systems; information retrieval; hypertext/hypermedia; version and edition management; distributed annotation and review systems; digital libraries, archiving, and preservation. We gratefully thank him for his generosity in funding this scholarship.''',
           'programs': ['bcs', 'cs', 'is'],
           'recipients': '''
<table class="scrollable" style="height: 300px">
<tr><th>Year</th><th>Recipients</th></tr>
<tr><td>2013/14</td><td>Jakob Gibson, Jackson VanHaitsma</td></tr>
<tr><td>2012/13</td><td>Patrick Crain, Jakob Gibson</td></tr>
<tr><td>2011/12</td><td>Thomas Wodarek, Patrick Crain</td></tr>
<tr><td>2010/11</td><td>Avery Martin, Thomas Wodarek</td></tr>
<tr><td>2009/10</td><td>Greg Clark, Avery Martin</td></tr>
</table>
'''
#        'appInfo': None
#         'applicationprocess': 'To Apply: Create an account or login on the <a href="http://153.106.116.135/" class="external"> First-Year Scholarships home page.</a> Then go to Computer Science Scholarships for First-Year Students.'
        },

        {'name': 'nyhoff',
          'ordinal': 0,         
           'shortDescription': ''' The Nyhoff scholarship is given to a strong first year computer science major or minor.''',
#            'shortDesc': '''The Larry and Sharlene Nyhoff Scholarship in Computer Science is funded by an endowment established by Dr. Larry Nyhoff. The scholarship is awarded to a strong first year student majoring or minoring in one of the computer science programs. Interested high school students should apply in January or early February of their senior year, before their first year at Calvin.''',
#            'details': '''Dr. Nyhoff is a professor emeritus of Calvin College. His teaching career at Calvin has spanned has more than 40 years. He has authored more than 30 textbooks, which are used in colleges and universities around the world. We gratefully thank him for his generosity in funding this scholarship.''',
           'programs': ['bcs', 'cs', 'is'],
           'recipients': '''
<table class="scrollable" style="height: 300px">
<tr><th>Year</th><th>Recipients</th>
<tr><td>2013/14</td><td>Jesse Bloomster</td></tr>
<tr><td>2012/13</td><td>James Lamine</td></tr>
</table>'''
#            'appInfo': None
#         'applicationprocess': 'To Apply: Create an account or login on the <a href="http://153.106.116.135/" class="external"> First-Year Scholarships home page.</a> Then go to Computer Science Scholarships for First-Year Students.'
           },
          

            {'name': 'cca',
          'ordinal': 5,             
           'title': 'CCA Computing Award',
           'shortDescription': '''The CCA computing award is given to the top graduating senior in computer science.''',
#            'shortDesc': '''The Department of Computer Science awards the CCA Computing Award (CCA) to its top graduate in computer science. The winners of this award since the founding the department in 1997/98 are shown here.''',
            'longDescription': '''The Department of Computer Science awards the CCA Computing Award (CCA) to its top graduate in computer science. The winners of this award since the founding the department in 1997/98 are shown here.''',
           'programs': ['bcs', 'cs'],
           'recipients': '''
<table class="scrollable" style="height: 300px">
<tr>
<th>Year</th>
<th>Recipient</th>
</tr>
<tr>
<td>2013</td>
<td>John Kloosterman & Ha Kyung Kong</td>
</tr>
<tr>
<td>2012</td>
<td>Peter Plantinga</td>
</tr>
<tr>
<td>2011</td>
<td>Nathaniel Burns & Ethan Van Andel</td>
</tr>
<tr>
<td>2010</td>
<td>Nathaniel Dykhuis & Jonathan Rosko</td>
</tr>
<tr>
<td>2009</td>
<td>Dan Brown</td>
</tr>
<tr>
<td>2008</td>
<td>Nathan Beach</td>
</tr>
<tr>
<td>2007</td>
<td>Joshua Holtrop</td>
</tr>
<tr>
<td>2006</td>
<td>Scott Admiraal & Andrew Meneely</td>
</tr>
<tr>
<td>2005</td>
<td>David Brondsema & Daniel Russcher</td>
</tr>
<tr>
<td>2004</td>
<td>Elliot Eshelman</td>
</tr>
<tr>
<td>2003</td>
<td>Matthew Post</td>
</tr>
<tr>
<td>2002</td>
<td>David Koop & David Vos</td>
</tr>
<tr>
<td>2001</td>
<td>Serita VanGroningen</td>
</tr>
<tr>
<td>2000</td>
<td>Abraham Fowler</td>
</tr>
<tr>
<td>1999</td>
<td>Jamie VanRandwyk</td>
</tr>
<tr>
<td>1998</td>
<td>Shawn Menninga & Thomas VanDrunen</td>
</tr>
</table>''',
           'appInfo':None},

           {'name': 'cisa',
          'ordinal': 6,
           'title': 'CISA Information Systems Award',
           'shortDescription': '''The CISA information systems award is given to the top graduating senior in information systems.''',
#            'shortDesc': '''The Department of Computer Science awards the CCA Computing Award (CCA) to its top graduate in computer science. The winners of this award since the founding the department in 1997/98 are shown here.''',
           'longDescription': '''The Department of Computer Science awards the CISA Information Systems Award (CCA) to its top graduate in information systems. The winners of this award since the award&rsquo;s inception are shown here.''',
           'programs': ['is'],
           'recipients': '''
<table class="scrollable" style="height: 300px">
<tr>
<th>Year</th>
<th>Recipient</th>
</tr>
<tr>
<td>2013</td>
<td>Gregory Vander Wal </td>
</tr>
<tr>
<td>2012</td>
<td>Nana Owusu Achau </td>
</tr>
<tr>
<td>2011</td>
<td>Taylor Bouman & Brian Derks </td>
</tr>
<tr>
<td>2010</td>
<td>Brent Sloterbeek</td>
</tr>
</table>
''',
           'appInfo':None},
            
            {'name': 'calvin',
          'ordinal': 8,             
           'title': 'Calvin-Wide Scholarships',
           'shortDescription': '''You can refer to the scholarship search database for more information on scholarships for Calvin students.''',
#            'shortDesc':None,
           'programs': ['bcs', 'cs', 'is', 'dc', 'ds'],
           'recipients':None,
           'appInfo':None,
           'url': 'http://www.calvin.edu/finaid/types/scholarships/search/'},
          
             {'name': 'external',
          'ordinal': 9,
           'title': 'External Scholarships',
           'programs': ['bcs', 'cs', 'is', 'dc', 'ds'],
           'shortDescription': 'The department maintains a list of external scholarship funding sources.',
           'longDescription': '''
           Here are some external scholarships that our students have applied for and/or received over the years:

<ul>
<li>
<a href="http://googleblog.blogspot.com/2010/12/2011-google-anita-borg-memorial.html" class="external">Google <em>Anita Borg Memory Scholarship</em></a>
<em> - for women, deadline is Feb 1 </em>
</li>
<li>
<em>
<a href="http://www.cra.org/Activities/craw/dmp/" class="external">CRA-W Distributed Mentoring program</a>
for women, due in early February
</em>
</li>
<em>
<li>
<a href="http://www.datatelscholars.org/" class="external">Datatel Scholars Foundation</a>
scholarships for all students, due in late January
</li>
<li>
<a href="http://www.microsoft.com/college/ss_overview.mspx" class="external">Microsoft Scholarships</a>
 a variety of scholarship types, due February 1
</li>
<li>
<a href="http://education.nasa.gov/edprograms/stdprograms/MUST_Scholarship_Project.html" class="external">NASA MUST Scholarship Project</a>
 focussed on minority students, due February 1
</li>
<li>
<a href="http://www.epo.usra.edu/usrp/" class="external">NASA Undergraduate Student Research Program</a>
 research-oriented, due in January and February
</li>
<li>
<a href="http://societyofwomenengineers.swe.org/" class="external">Society of Women Engineers</a>
 for women
</li>
<li>
<a href="http://www.associationforsoftwaretesting.org/drupal/sigs/scholarship/uesta" class="external"> Undergraduate Excellence in Software Testing Award</a>
 for any student interested in software testing
</li>
<li>
<a href="http://www.braintrack.com/degree-programs-and-certifications/articles/computer-science-degree-programs#" class="external">BrainTrack Computer Science Degree Scholarships</a>
 $1,000 and $500 scholarships for students majoring in CS or IT. Scholarships are awarded twice per year; submission deadlines are Nov 1 and March 1 each year.
</li>
<li>
<a href="http://www.hartfordrents.com/scholarship" class="external"> Hartford Technology Rental Co. IT Scholarship</a>
 for any student majoring in an IT related field, $1,000 awarded two times annually, December & May
</li>
</em>
</ul>
           
           ''',
           'recipients':None,
           'appInfo': 'The rules and restrictions on these scholarships vary. Apply for them directly at the given websites.'
           },

         {'name': 'hommes', 'ordinal': 4},
         {'name': 'grateful', 'ordinal': 4},
         {'name': 'tools', 'ordinal': 4},
         {'name': 'duthler', 'ordinal': 4},
         {'name': 'open', 'ordinal': 4},
         {'name': 'spectrum', 'ordinal': 4},
         ],

          # articles...
          [

           {'name': 'news_4',
         'title': 'A New CS Department Website',
         'summary': 'The Department launches a new, responsive website',
         'content': '''The Department of Computer Science has launched a new department website.
         The new site is based on tools developed by CIT that make the site responsive different device profiles.
         Let us know what you think by going to the contacts page and sending your comments and/or questions.''',
         'date': datetime.strptime('2014-9-1', '%Y-%m-%d')
        },
           {'name': 'news_3',
            'title': 'January Interim Course in Thailand',
            'summary': 'The department offers an off-campus interim in Thailand',
            'content': '''The Department of Computer Science is offering an overseas, 
            mission-oriented interim course for January, 2015. We will visit Chiang Mai, 
            in northern Thailand, and participate in software development for 
            cross-cultural, Christian applications. For more information, 
            see <a href="/courses/cs/W60/">CS W60 - Christian Computing in Thailand</a>.
''',
         'date': datetime.strptime('2014-8-25', '%Y-%m-%d')
            },
           {'name': 'news_2',
            'title': 'Start Planning Now for Your Summer 2015 Internship',
            'summary': 'Plan now for your summer 2015 internship',
            'content': '''There are lots of summer internship opportunities here in W. Michigan.
Attending Calvin's annual
<a href="http://www.calvin.edu/career/engineering-computing-fair.html" class="external">CS &amp; Engineering Career Fair</a>
will allow you to network with potential employers and possibly land one.
Prof. Bailey, the CS department's <em>Internship Coordinator</em> can also offer good advice.
<p>
There are also 
<a href="http://www.businessinsider.com/insane-salaries-for-tech-interns-2013-12?op=1http://www.businessinsider.com/insane-salaries-for-tech-interns-2013-12?op=1" class="external">amazing opportunities at many tech companies in Silicon Valley</a>.
<p>
If you'd like to pursue an internship with one of these companies,
start building your resume now by taking CS courses and pursuing one or more innovative personal projects that will make you an attractive prospect for these companies.
''',
         'date': datetime.strptime('2014-8-14', '%Y-%m-%d')
            },
           {'name': 'news_1',
            'title': 'High Demand for CS Talent in W. Michigan',
            'summary': 'CS talent is in high demand in W. Michigan',
            'content': '''Check out 
<a href="http://www.rapidgrowthmedia.com/features/073114techtalent.aspx" class="external">
this recent article</a>
about the technology-related careers in W. Michigan,
and the high demand for people with advanced computing skills. 
<p>
For information about career options nation-wide, check out our
<a href="http://cs.calvin.edu/documents/computing_careers">
Computing Careers Market</a> page.
''',
         'date': datetime.strptime('2014-8-14', '%Y-%m-%d')
            },
           {'name': 'news_0',
            'title': 'Prof. Adams Writes Two New Books',
            'summary': '2 new books published by Prof. Adams',
            'content': '''
Prof. Adams has written two new introductory programming books, 
using the latest version of
<a href="http://alice.org" class="external">Alice</a>:
<ul>
 <li>
   <a href="http://www.cengage.com/search/productOverview.do?Ntt=Adams%7C%7C1228789950182208363114811459211567683698&N=16&Ntk=APG%7C%7CP_EPI&Ntx=mode%2Bmatchallpartial" class="external">Alice 3 in Action: Computing Through Animation</a>,
a 6-chapter introduction to animation, programming, and story-telling.
 <li>
  <a href="http://www.cengage.com/search/productOverview.do?Ntt=Adams||152186095413013658964247434272051974501&N=16&Ntk=APG%7C%7CP_EPI&Ntx=mode%2Bmatchallpartial" class="external">Alice 3 in Action with Java</a>,
a 14-chapter introduction to programming; six with Alice 3 and eight with Java.
</ul>
Both books introduce students to object-oriented programming concepts, including object-oriented design, objects and methods, control structures, data structures, and events.
<p>
Alice is 3D animation software from 
<a href="http://www.cmu.edu/index.shtml" class="external">Carnegie Mellon</a> that lets people build
sophisticated 3D animations in Java, 
using a drag-and-drop integrated development environment that eliminates syntax errors.
<p>
The new version uses 3D models donated by 
<a href="http://www.ea.com/" class="external">Electronic Arts</a>,
from its "The Sims" line of games.''',
         'date': datetime.strptime('2014-8-25', '%Y-%m-%d')            
            }
        ],

        # counters...
        [
         {'name': 'news', 'count': 3},
         {'name': 'images', 'count': 0},
         {'name': 'documents', 'count': 0},
         {'name': 'scholarships', 'count': 7}
        ],
        #Tech News Words
        [
         {'name':'tech_news_good',
          'data':
              '''calvin college
calvin college
Joel Adams
Victor Norman
Keith VanderLinden
Harry Plantinga
Randall Prium
Michael Stob
Earl Fife
David Laverell
Christian Classics Ethereal Library
Nyna Sykes
Brian Vanderwal
Will Groenendyk
Will Groenendyk
Sharon Gould
Larry Nyhoff
Sanford Leestma
Serita Nelesen
Patrick Bailey
Computer Science
Big Data
High Performance Computing
AI
Artificial intelegence
Database
Website
Statistics
Jobs
calvin college
calvin college
Joel Adams
Victor Norman
Keith VanderLinden
Harry Plantinga
Randall Prium
Michael Stob
Earl Fife
David Laverell
Christian Classics Ethereal Library
Nyna Sykes
Brian Vanderwal
Will Groenendyk
Will Groenendyk
Sharon Gould
Larry Nyhoff
Sanford Leestma
Serita Nelesen
Patrick Bailey
Computer Science
Big Data
High Performance Computing
AI
Artificial intelegence
Database
Website
Statistics
Jobs
                '''},
            {'name':'tech_news_bad',
             'data':'''hope bad
grand valley'''}]
  ]
