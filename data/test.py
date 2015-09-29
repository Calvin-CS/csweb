'''
This data structure provides a hard-coded starting point for unit tests.

Created on Jan 23, 2014

@author: kvlinden
'''
from datetime import datetime

from passlib.apps import custom_app_context

data = [

    # programs...
    # The test needs to define the bada program so that the hard-coded
    # list of programs in units/programs.py can find it. Add the other
    # programs as well so the program name can be set properly.
    [{'name': 'bcs',
      'title': 'bcs title'
      },
     {'name': 'bacs',
      'title': 'bacs title'
      },
     {'name': 'bais',
      'title': 'bais title'
      },
     {'name': 'badc',
      'title': 'badc title'
      },
     {'name': 'bada',
      'title': 'bada title'
      }
     ],

    # documents...
    [{'name': 'document1',
      'title': 'document1 title',
      'content': 'document1 content'
      }],

    # resources...
    [{'name': 'resource1',
      'title': 'resource1 title',
      'content': 'resource1 content'
      }],

    # departments...
    [{'name': 'cs',
        'title': 'cs name',
        'tagline': 'cs tagline',
        'shortDescription': 'cs short description',
        'longDescription': 'cs long description'
      }],

    # users...
    [{'name': 'user',
      'password': custom_app_context.encrypt('password')
      }],

    # images...
    [{'name': 'image_0',
      'filename': 'image_0.jpg',
      'description': 'image_0 description',
      'tags': ['departments.cs']},
     {'name': 'image_1',
      'filename': 'image_1.jpg',
      'description': 'image_1 description',
      'tags': ['other']
      }],

    # scholarships...
    [  {'name': 'scholarship1',
        'ordinal': 0,
           'title': 'scholarship1 title',
           'shortDescription': '''scholarship1 short description''',
           'programs': ['bada', 'bacs', 'bais'],
           'recipients': '''scholarship1 past recipients''',
           'applicationInfo': None
        },

      ],

    # articles...
    [{'name': 'news_0',
      'title': 'news_0 title',
      'summary': 'news_0 teaser',
      'content': '''news_0 content''',
      'date': datetime.strptime('1996-9-1', '%Y-%m-%d')
      },
     {'name': 'news_1',
      'title': 'news_1 title',
      'summary': 'news_1 teaser',
      'content': '''news_1 content''',
      'date': datetime.strptime('2014-1-1', '%Y-%m-%d')
      }
     ],

    # counters...
    [{'name': 'news', 'count': 3},
     {'name': 'images', 'count': 0},
     {'name': 'documents', 'count': 0}
     ],

    # Tech News Words
    [{'name': 'tech_news_good', 'data': 'good1 good2'},
     {'name': 'tech_news_bad', 'data': 'bad1 bad2'}]
]
