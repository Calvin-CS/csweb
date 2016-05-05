See the department Confluence page for system notes:
    https://wiki.calvin.edu/pages/viewpage.action?pageId=26411289

Configuring and Running CSWeb
- I generally followed these instructions to configure the system tools:
	http://www.eightytwo.com.au/notes/linux/webserver-setup-guide/
	https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-14-04

Machines:
- cs.calvin.edu (153.106.116.6)
    the production server
    CS password access (no public key access via Bitvise yet - Chris plans to change this)
    Still on Ubuntu 12.
- cs-dev.cs.calvin.edu (153.106.116.18)
    the development server
    public key access over Calvin VPN via Bitvise (see system notes for Bitvise).
    Questions:
        Why is the system pre-loaded with student accounts? This should be a cs.calvin.edu development server only.
- teamcity.cs.calvin.edu
    TeamCity server
    Access? I've installed public keys for both my machines on https://freeipa1.cs.calvin.edu but it only works at the office, not at home.
    Configure via TC's web interface.
- teamcityba-1.cs.calvin.edu
    TeamCity build agent
    public key access over Calvin VPN via Bitvise
    If we want to run unittests before deployment this server should be built in the same way as {cs|cs.dev}.calvin.edu.
        Eventually, we'll add cs262-dev/teamcityba-2 pair for cs262 projects (i.e., PostgresSQL, J2EE, etc.).
- Note that the cs, cs-dev (and teamcityba?) servers need a bauser account that can
    write to the appropriate directories
    restart the servers
    See https://confluence.jetbrains.com/display/TCD9/Setting+up+and+Running+Additional+Build+Agents#SettingupandRunningAdditionalBuildAgents-Prerequisites

Useful commands:
	netstat -lnptu
	ps -aux

Tools
- Mongo 3.2 (create the csweb users to authenticate/authorize on the csweb db. See the Confluence page).
    mongo -u csweb -p COURSE_PASSWD csweb
        show collections
        db.COLLECTION.find()
        exit
    How should we handle the production database?
        Scripts will copy the current version of the database from the production server to this server.
        Process for csweb db upgrade:
            1. Turn off the db copy (prod->dev) script (or at least ensure that it won't run during testing/deployment).
            2. Deploy new csweb to cs-dev.
            3. Modify the dev machine's copy of the current db for the new structure required by the new csweb.
            4. Manually copy the dev machine's db to the production machine.
            5. Deploy new csweb to cs.
            6. Turn of the db copy (prod->dev) script.

- Nginx

- uWSGI

- Flask

- Git/GitHub
    https://github.com/Calvin-CS/csweb
    Branches:
        master - basic work
        development - TC auto-deploys this branch to cs-dev.cs.calvin.edu (the development server)
        production - TC auto-deploys this branch to cs.calvin.edu (the live production server)
    To deploy development version:
        1. Develop new features on master (or other work) branches.
        2. Merge current master version into the development branch.
        3. Commit/push development branch to GitHub.
    To deploy the production version:
        1. Make sure that all the key changes made to the development branch are merged back into master.
        2. Repeat the deployment process listed above but target the production branch.

- TeamCity
    Build agent is specified here: TC->projects->DeptWebsite->CompatibleAgents
        ->Details
            hostname, IP, port, etc.
        TC appears to configure system/file access to this agent automatically.
    Build configuration is specified here: TC->projects->DeptWebsite->Settings
        ->VCSettings
            specified a VCroot:
                URL: https://github.com/Calvin-CS/csweb.git
                branch: refs/heads/development
        ->BuildStep:Ant
            Specifies the runner type (ant) and the steps in the build process.
                For now, the build agent will simply download code from GitHub, copy it to cs-dev and restart the cs-dev servers.
                This can be done with a single Ant script target based on the build file (build/build.xml).
                Ant script needs to include command to kick uWSGI on cs-dev
                    ssh bauser@cs-dev "the command"
                as follows:
	                <target name="upload" depends="package">
        		        <exec dir="${build.uploadPath}" executable="ssh" failonerror="true">
		        	        <arg value="${upload.credentials}" />
			                <arg value="the command" />
        		        </exec>
        	        </target>
            Use Ant for deployment for now; Gradle is designed for Java (CS 262?)
        ->Triggers
            specifies default trigger for build (on checkin to VCSroot)
        ->Parameters (specified here rather than in build.xml so that they don't get uploaded to GitHub)
            ${upload.credentials} (NB. Hirt built a bauser account on ba-1 and on cs-dev solely for the purpose of deploying files.)
            ${upload.destination} (i.e., the development server, bauser@cs-dev:/srv/www/calvin.edu/csweb (needs to change))


Old Tool Notes
---------------------------------------------------------------------
- Mongo: 2.4.9
	Installed MongoDB as shown here: 
		http://docs.mongodb.org/manual/tutorial/install-mongodb-on-debian/
		...but used the configuration file settings from the 82 site shown above.
			I added auth, fork and bind_ip values to the configuration.
			I redirected the data to /data/db and the log to /data/mongodb.log. 
			It turns out the the fork=true causes a bug in the stop script so I took that out.
				See https://jira.mongodb.org/browse/SERVER-7254.
	Files/Directories:
		/etc/init.d/mongodb                     (control script, e.g., start/stop)
		/data/db                                (data directory)
		/data/mongodb.log                       (log file)
	Commands (run as root):
		/etc/init.d/mongodb start             (starts the server, I believe)
	To test/run mongo in commandline mode on the server, do the following as a normal user:
		mongo
		use csweb
		show collections
		db.counters.find()
		...
		exit
	I initialized/updated the server database by editing/uploading/running utils/init_csweb.py.
	There are separate development and testing databases initialized on-the-fly by data/*.py.
	Backup/Restore:
		login as root and run:
			mongobackup -db csweb -o /data/dumps/<date>
				This creates a backup subdirectory (e.g., dumps/2014-08-22)
			mongorestore <backup> 
				This restores the data stored in the dump subdirectory (e.g., /data/dumps/2014-08-22/csweb).
		For details, see: http://blogs.lessthandot.com/index.php/datamgmt/dbadmin/mssqlserveradmin/mongodb-backup-and-restore-databases/
	

---------------------------------------------------------------------
- Nginx: 1.4.4
	Files/Directories:
		/opt/nginx                            (installation directory)
		/etc/init.d/nginx                     (control script, e.g., start/stop)
		/srv/www/calvin.edu/                  (web materials directory)
		/srv/www/calvin.edu/logs/*            (log files)
	Commands (run as root): 
		/etc/init.d/nginx start               (starts the server, I believe)	
		/opt/nginx/sbin/nginx -s reload       (reloads the config for a running Nginx)
	Config file: /opt/nginx/conf/nginx.conf
	    See utils/nginx.conf


---------------------------------------------------------------------
- uWSGI: 2.0
	Files/Directories:
		??                                    (installation directory)
		/etc/init.d/uwsgi                     (control script, e.g., start/stop)
		/etc/default/uwsgi                    (default settings file, including python venv)
		/var/log/uwsgi.log                    (log file)
	Installed uWSGI generally as described in the 82 site above. Notes:
	    This required that I run % apt-get install python-dev
	    Removed the "4" from the "-M 4" in the suggested /etc/init.d/uwsgi script. 
	    	It must no longer be supported in uWSGI 2.0.
	    Used --check-static and --static-index to configure static file from /. 
	      	See /etc/init.d/uwsgi.
	    See uwsgi logs in /var/log/uwsgi.log.
	Commands (run as root):
		/etc/init.d/uwsgi start                        (Starts uWSGI) 
		/etc/init.d/uwsgi restart                      (Restarts uWSGI, cf. utils/deploy.txt)


---------------------------------------------------------------------
- Python: 2.7.3
	This may have already been installed in Linux, otherwise, I did a standard install.
	Files/Directories:
		/srv/www/calvin.edu/csweb/venv        (virtual environment installed here)
			Includes at least the following: flask, flask_mail, flask_pymongo, flask_wtf, flask_testing, itsdangerous, passlib, pymongo, requests, wtforms
			Technews required further Python libraries (see below).

---------------------------------------------------------------------
- Flask 0.10.1
	This is installed in the Python venv described above.
	Files/Directories:
		/srv/www/calvin.edu/csweb             (Flask web application code and resources)
	Run deploy_prod.py to copy the web application files into this directory.
	

------------------------------------------------------------------------
-newsSearch Info
The Algorithm is specified in the technews_notes.txt file.
The database stores 3 news articles that are displayed on the home page.  Also it stores the 2 database entries containing an instance of all the words that have been parts of the summary and title of the news articles that have received an up/down indication  Retrieving the latest news list as well as the latest states are run on the fly.
List of Pages
	./index.html
			This page, the home page displays a list of a "random" selection of 3 of the top 11 news articles that were gathered for the day. A cron job will re-populate these articles daily.
	The following pages require a user to be logged on.
		./admin/news
			Along with the other department news tech_news x (1-3) are displayed, generally towards the top because the list is populated based off last date. By selecting the up/down button in this section, the database asynchronously, and refresh the current homepage news items to reflect the latest stats.
		./admin/technews
			This page displays a list of all the current tech news.  The server goes out to all the RSS feeds, pulls the data, and ranks the news articles
		./admin/technews/refresh 
			This page first refreshes the 3 current list of three news articles and then displays the full list to the administrator.
	./admin/technews/<<article link>>/up
	./admin/technews/<<article link>>/down
			These links indicate whether an article is considered good or bad.
	./admin/technews/<<article link>>/up/refresh
	./admin/technews/<<article link>>/down/refresh
		These links also indicate if an article is good or bad, as well as refresh the current list of articles displayed on the home page.
	
	the utility files and what they do
	
		utils.update_csweb
			This file is meant to be run by a cron job.  It logs into csweb, and then calls the ./admin/technews/refresh page to get the new data and recalculate the stats.
			See http://stackoverflow.com/questions/4460262/running-a-python-script-with-cron for mor inforamtion on how to set up the cron job
		/app/findTechNews.py
			This file is the main �brains� behind most of the functionality of this feature.  The readRSS contains some logic to only get more recent articles.
	 
	pointers to files that code important things (e.g., the news feed list)
		/csweb/app/static/rssfeeds.txt
			News feeds list.
		/app/utilities
			This file contains multiple functions for the project.
			create_news_list and create_newsarticle_list � displays the technews with the other onsite news articles
			create_techNewsarticle_list � creats the article list for tech news by itself (used for admins).
		/app/units/tech_news.py
			This file contains the unit definition similar to the local news articles.  This calls the app. findTechNews functions but mostly handles database operations.
		/app/views.py
			This file handles the calls to the different web pages.  All the realvent functions have tehcnews in their name.	
		/app/static/rssfeeds.txt
			This file is a list of all the news feeds that we are pulling from.
	the system requirements (e.g., Python numpy):
	This is a list of all the imports that I have, but not sure which ones might be included by default.
		The code for this system is written in Python.
		Libraries needed: urllib, urllib2, cookielib
			from __future__ import division
			from functools import wraps
			from decimal import *
			import json
			from pprint import pprint
			import feedparser
			from xml.dom import minidom, Node
			import time
			from datetime import datetime, timedelta, date
			import numpy as np
			from sklearn.naive_bayes import GaussianNB
			from utils.analyzeText import analyzeText
			import string
			from flask.globals import g
			from wtforms.fields.simple import TextField, TextAreaField, HiddenField
			from random import randrange

	List got from trial from 'scratch' linxu install -- Didn't actully get it working because mongodb wasn't installed.
	Note for these to work on the server's python virtual environment, we must use ./pip from the venv folder. 
		passlib (pip)
		numpy -- had to install via .exe for windows unix: (apt-get install)
		scipy -- This required doing the following:
			apt-get install python-scipy
			apt-get build-dep python-scipy
			./pip install scipy
		feedparser  (pip)
		twill (pip)
		cssselect (pip)
		urllib2 (pip)
		lxml   (pip)
		scikit-learn (apt-get install)
		cython (apt-get install)
