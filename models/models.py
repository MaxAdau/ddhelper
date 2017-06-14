# coding: utf-8

import sqlalchemy
from sqlalchemy.orm import backref, relationship

from database import Base

'''
class Department(Base):
    __tablename__ = 'department'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
'''



# TODO add all fields of this class, matching postgresql
class Race(Base):
    """Model for the race table"""
    __tablename__ = 'races'

    # incremental ID
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)

    # About the race
    name = sqlalchemy.Column(sqlalchemy.String)
    description = sqlalchemy.Column(sqlalchemy.String)

    # TODO move it to an ENUM type
    size = sqlalchemy.Column(sqlalchemy.String)

    def __repr__(self):
        return self.name


class Class(Base):
    __tablename__ = 'classes'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    description = sqlalchemy.Column(sqlalchemy.String)




class Character(Base):
    __tablename__ = 'chars'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    # Use default=func.now() to set the default hiring time
    # of a Character to be the current time when an
    # Character record was created


    race_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('races.id'))
    klass_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('classes.id'))
    race = relationship(Race)
    klass_ = relationship(Class)

'''
import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean

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

    # Hit point
    hp = Column(Integer)

    def __repr__(self):
        return self.name


class Weapon(BaseModel, db.Model):
    """Model for the weapon table"""
    __tablename__ = 'weapons'

    # incremental ID
    id = Column(Integer, primary_key=True)

    # About the weapon
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


class Armor(BaseModel, db.Model):
    """Model for the armor table"""
    __tablename__ = 'armors'

    # incremental ID
    id = Column(Integer, primary_key=True)

    # Is this armor a shield ?
    is_shield = Column(Boolean)

    # About the armor
    name = Column(String)
    description = Column(String)

    # Damage
    ca_bonus = Column(Integer)
    max_dex = Column(Integer)
    armor_penalty_check = Column(Integer)
    arcane_spell_fail = Column(Integer)
    speed_6m = Column(Integer)
    speed_9m = Column(Integer)

    # Other
    weight = Column(Float)  # in Kilo
    dmg_type = Column(String)
    cost = Column(String)  # in GP

    def __repr__(self):
        return self.name


class Event(BaseModel, db.Model):
    """Model for the armor table"""
    __tablename__ = 'events'

    # incremental ID
    id = Column(Integer, primary_key=True)

    # About the event
    name = Column(String)
    adventure_id = Column(Integer, ForeignKey("adventures.id"))
    adventure = db.relationship("Adventure")

    # what did happen here ?
    description = Column(String)

    def __repr__(self):
        return self.name


class Encounter(BaseModel, db.Model):
    """Model for the armor table"""
    __tablename__ = 'encounters'

    # incremental ID
    id = Column(Integer, primary_key=True)

    adventure_id = Column(Integer, ForeignKey("adventures.id"))
    adventure = db.relationship("Adventure")

    # About the event
    name = Column(String)
    description = Column(String)

    # Who did fight ?
    players = Column(String)  # TODO this should be a list of character IDs where character.type == PC
    allies = Column(String)  # TODO this should be a list of character IDs
    opponents = Column(String)  # TODO this should be a list of character IDs

    def __repr__(self):
        return self.name


class Adventure(BaseModel, db.Model):
    """Model for the adventure table"""
    __tablename__ = 'adventures'

    # incremental ID
    id = Column(Integer, primary_key=True)

    name = Column(String)
    description = Column(String)

    # History of this adventure
    events = Column(String)  # TODO this should be a list of events.id
    encounters = Column(String)  # TODO this should be a list of encounter.id
    #race_id = Column(Integer, ForeignKey("races.id"))
    #race = db.relationship("Race")

    players = Column(String)  # TODO this should be a list of players.id

    def __repr__(self):
        return self.name
'''
