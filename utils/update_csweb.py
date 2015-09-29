#!/srv/www/calvin.edu/csweb/venv/bin/python

# This script modifies the csweb production database (using update or insert).
# Load it into /data/update_csweb.py and run it manually from there.

# For more information on PyMongo updates, see:
#   http://api.mongodb.org/python/current/api/pymongo/collection.html#pymongo.collection.Collection.update

import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.csweb

# db.wordBank.update(
#                    {'name': 'tech_news_good'},
#                    {'$set': {'data': '''
# calvin college
# Joel Adams
# Victor Norman
# Keith VanderLinden
# Keith Vander Linden
# Harry Plantinga
# Randall Prium
# Michael Stob
# Earl Fife
# David Laverell
# Christian Classics Ethereal Library
# Jobs
# Big Data
# High Performance Computing
# AI
# Artificial intelligence
# '''}})
# db.wordBank.update(
#                    {'name': 'tech_news_bad'},
#                    {'$set': {'data': '''horrible'''}})

# db.news.update(
#     # Query...
#     {'name': 'news_4'},
#     # Update...
#     {'$set': {'title': 'A New CS Department Websiteee'}}
#     )

# db.programs.update(
#     # Query...
#     {'name': 'bada'},
#     # Update...
#     {'$set': {'majorDescription': '''
# <p>The Interdisciplinary Major in Art and Computer Science is designed for students who have interests in art, 
# computers and digital media. Other colleges might call this major program &ldquo;Digital Art&rdquo;, &ldquo;Digital Imaging&rdquo;, 
# or &ldquo;Digital Media&rdquo;.</p>
# <p>It is an interdisciplinary major and thus must be approved by the departments 
# from which the courses are drawn, but the Departments of Computer Science and Art worked together 
# to create this major and routinely approve interdisciplinary program proposals that include these courses.</p>
# '''}}
#     )

