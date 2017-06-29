# coding: utf-8
# !/usr/bin/env python

import os

from flask import Flask
from flask_graphql import GraphQLView
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from models.schema import schema
from models.models import *
from database import db, POSTGRES, db_session

app = Flask(__name__)
app.debug = True

# TODO move it in a config file
app.secret_key = "super secret key"

# Set upAdmin flask
admin = Admin(app, name='Dungeons and Dragons', template_mode='bootstrap3')

# Add views of flask admin UI
admin.add_view(ModelView(Event, db.session))
admin.add_view(ModelView(EventActor, db.session))
admin.add_view(ModelView(Actor, db.session))
admin.add_view(ModelView(Location, db.session))

# Define postgresql config
if 'DDH_DATABASE_PASSWD' not in os.environ:
    exit('Unable to find DDH_DATABASE_PASSWD env variable : exiting')

# Setup Flask app to reach postgresql base
# TODO should use a config file ... at least database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config['DEBUG'] = True

# Connect SQLAlchemy object with Flask application
db.init_app(app)

# Set up GraphQLView

# Should this realy be here ?
# default_query = '''
#   query {
#     event {
#       node {
#         id,
#         name,
#         description
#     }
# '''

default_query = '''
  allEvents (first :1) {
    edges {
      cursor
      node {
        id
        name
        date
        description
        location {
          id
          name
          description
        }
        presentActors {
          id
          name
        }
      }
    }
  }
}'''.strip()


app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        default_query=default_query,
        graphiql=True,

        # This is needed to be able to get a context in schema.Query typt
        # ex : SCHEMA.get_query(context)
        # Otherwise, I got the error : Request has no attribute get
        # https://github.com/graphql-python/graphene-sqlalchemy/issues/30
        context={'session': db_session}
        ),
    )


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    #init_db()
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)