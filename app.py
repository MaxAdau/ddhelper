# coding: utf-8
# All of this code came from here
# https://www.theodo.fr/blog/2017/03/developping-a-flask-web-app-with-a-postresql-database-making-all-the-possible-errors/

#!/usr/bin/env python

# This code came from here ; http://docs.graphene-python.org/projects/sqlalchemy/en/latest/tutorial/
import os
from flask import Flask

from database import db_session
from flask_graphql import GraphQLView
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from models.schema import schema
from models.models import *
from models.events_models import *
from database import db, POSTGRES

app = Flask(__name__)
app.debug = True
app.secret_key = "super secret key"

# Set upAdmin flask
admin = Admin(app, name='Dungeons and Dragons', template_mode='bootstrap3')

# Add views of flask admin UI
admin.add_view(ModelView(Character, db.session))
admin.add_view(ModelView(Race, db.session))
admin.add_view(ModelView(Klass, db.session))
admin.add_view(ModelView(Weapon, db.session))
admin.add_view(ModelView(Armor, db.session))
admin.add_view(ModelView(Event, db.session))
admin.add_view(ModelView(Encounter, db.session))
admin.add_view(ModelView(Adventure, db.session))

# Define postgresql config
if 'DDH_DATABASE_PASSWD' not in os.environ:
    exit('Unable to find DDH_DATABASE_PASSWD env variable : exiting')

# Setup Flask app to reach postgresql base
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://DB_USER:PASSWORD@HOST/DATABASE'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config['DEBUG'] = True

# Connect SQLAlchemy object with Flask applicatoin
db.init_app(app)




# Set up GraphQLView
default_query = '''
{
  allEmployees {
    edges {
      node {
        id,
        name,
        department {
          id,
          name
        },
        role {
          id,
          name
        }
      }
    }
  }
}'''.strip()


app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()



if __name__ == '__main__':
    #init_db()

    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

'''
import argparse
import os

from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import os

from models.models import db, Race, Class, Weapon, Armor, Event, Adventure, Encounter
from models.character import Character

# Create Flask app
app = Flask(__name__)
app.secret_key = "super secret key"

# Admin flask
admin = Admin(app, name='Dungeons and Dragons', template_mode='bootstrap3')

# Add views of flask admin UI
admin.add_view(ModelView(Character, db.session))
admin.add_view(ModelView(Race, db.session))
admin.add_view(ModelView(Class, db.session))
admin.add_view(ModelView(Weapon, db.session))
admin.add_view(ModelView(Armor, db.session))
admin.add_view(ModelView(Event, db.session))
admin.add_view(ModelView(Encounter, db.session))
admin.add_view(ModelView(Adventure, db.session))

# Define postgresql config
if 'DDH_DATABASE_PASSWD' not in os.environ:
    exit('Unable to find DDH_DATABASE_PASSWD env variable : exiting')


POSTGRES = {
    'user': 'nndtlkswctupow',
    'pw': os.environ['DDH_DATABASE_PASSWD'],
    'db': 'dalp11jeof21vd',
    'host': 'ec2-54-75-231-195.eu-west-1.compute.amazonaws.com',
    'port': '5432'
}

# Setup Flask app to reach postgresql base
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://DB_USER:PASSWORD@HOST/DATABASE'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config['DEBUG'] = True

# Connect SQLAlchemy object with Flask applicatoin
db.init_app(app)

@app.route('/')
def hello():
    return "Hello World!"


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
