import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy

# TODO move it to config.py
POSTGRES = {
    'user': 'zqhpnstbycewhx',
    'pw': os.environ['DDH_DATABASE_PASSWD'],
    'db': 'd4lohv9deu7e4b',
    'host': 'ec2-54-246-108-119.eu-west-1.compute.amazonaws.com',
    'port': '5432'
}

db_url = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
# DEBUG print(db_url)
engine = create_engine(db_url,
                        convert_unicode=True)

#engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

# TODO  make a fixture
'''def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from models.models import Department, Employee, Role
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # Create the fixtures
    engineering = Department(name='Engineering')
    db_session.add(engineering)
    hr = Department(name='Human Resources')
    db_session.add(hr)

    manager = Role(name='manager')
    db_session.add(manager)
    engineer = Role(name='engineer')
    db_session.add(engineer)

    peter = Employee(name='Peter', department=engineering, role=engineer)
    db_session.add(peter)
    roy = Employee(name='Roy', department=engineering, role=engineer)
    db_session.add(roy)
    tracy = Employee(name='Tracy', department=hr, role=manager)
    db_session.add(tracy)
    db_session.commit()'''

# Setup Flask app to reach postgresql base
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://DB_USER:PASSWORD@HOST/DATABASE'



# Initialize a database object
# Could be moved to a model.py file
db = SQLAlchemy()
