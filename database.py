import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy

POSTGRES = {
    'user': 'zqhpnstbycewhx',
    'pw': os.environ['DDH_DATABASE_PASSWD'],
    'db': 'd4lohv9deu7e4b',
    'host': 'ec2-54-246-108-119.eu-west-1.compute.amazonaws.com',
    'port': '5432'
}

# This is exported as a conf variable ... not very clean
db_url = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

# DEBUG print(db_url)
engine = create_engine(db_url,
                        convert_unicode=True)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

# Instantiate my Base Type
Base = declarative_base()

# Initialize a database object
# Could be moved to a model.py file
db = SQLAlchemy()
