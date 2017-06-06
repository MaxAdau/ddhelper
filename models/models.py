# coding: utf-8

import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Float

# Initialize a database object
# Could be moved to a model.py file
db = SQLAlchemy()


class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True

    def __init__(self, *args):
        super(BaseModel, self).__init__(*args)

class Race(BaseModel, db.Model):
    """Model for the race table"""
    __tablename__ = 'races'

    # incremental ID
    id = Column(Integer, primary_key=True)

    # About the race
    name = Column(String)
    description = Column(String)

    # TODO move it to an ENUM type
    size = Column(String)

    def __repr__(self):
        return self.name


class Class(BaseModel, db.Model):
    """Model for the class table"""
    __tablename__ = 'classes'

    # incremental ID
    id = Column(Integer, primary_key=True)

    # About the race
    name = Column(String)
    description = Column(String)

    def __repr__(self):
        return self.name


class Weapon(BaseModel, db.Model):
    """Model for the weapon table"""
    __tablename__ = 'weapons'

    # incremental ID
    id = Column(Integer, primary_key=True)

    # About the race
    name = Column(String)
    description = Column(String)

    # Damage
    dmg_S = Column(String)
    dmg_M = Column(String)
    critical = Column(String)
    range_increment = Column(Integer) # in meter

    # Other
    weight = Column(Float) # in Kilo
    dmg_type = Column(String)
    cost = Column(String) # in GP

    def __repr__(self):
        return self.name
