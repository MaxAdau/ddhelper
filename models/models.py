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
    hp = sqlalchemy.Column(sqlalchemy.Integer)

    def __repr__(self):
        return self.name


class Character(Base):
    __tablename__ = 'chars'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)

    race_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('races.id'))
    klass_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('classes.id'))
    race = relationship(Race)
    klass_ = relationship(Class)

class Weapon(Base):
    """Model for the weapon table"""
    __tablename__ = 'weapons'

    # incremental ID
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)

    # About the weapon
    name = sqlalchemy.Column(sqlalchemy.String)
    description = sqlalchemy.Column(sqlalchemy.String)

    # Damage
    dmg_S = sqlalchemy.Column(sqlalchemy.String)
    dmg_M = sqlalchemy.Column(sqlalchemy.String)
    critical = sqlalchemy.Column(sqlalchemy.String)
    range_increment = sqlalchemy.Column(sqlalchemy.Integer) # in meter

    # Other
    weight = sqlalchemy.Column(sqlalchemy.Float) # in Kilo
    dmg_type = sqlalchemy.Column(sqlalchemy.String)
    cost = sqlalchemy.Column(sqlalchemy.String) # in GP

    def __repr__(self):
        return self.name

class Armor(Base):
    """Model for the armor table"""
    __tablename__ = 'armors'

    # incremental ID
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)

    # Is this armor a shield ?
    is_shield = sqlalchemy.Column(sqlalchemy.Boolean)

    # About the armor
    name = sqlalchemy.Column(sqlalchemy.String)
    description = sqlalchemy.Column(sqlalchemy.String)

    # Damage
    ca_bonus = sqlalchemy.Column(sqlalchemy.Integer)
    max_dex = sqlalchemy.Column(sqlalchemy.Integer)
    armor_penalty_check = sqlalchemy.Column(sqlalchemy.Integer)
    arcane_spell_fail = sqlalchemy.Column(sqlalchemy.Integer)
    speed_6m = sqlalchemy.Column(sqlalchemy.Integer)
    speed_9m = sqlalchemy.Column(sqlalchemy.Integer)

    # Other
    weight = sqlalchemy.Column(sqlalchemy.Float)  # in Kilo
    dmg_type = sqlalchemy.Column(sqlalchemy.String)
    cost = sqlalchemy.Column(sqlalchemy.String)  # in GP

    def __repr__(self):
        return self.name


class Event(Base):
    """Model for the armor table"""
    __tablename__ = 'events'

    # incremental ID
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)

    # About the event
    name = sqlalchemy.Column(sqlalchemy.String)
    adventure_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("adventures.id"))
    adventure = relationship("Adventure")

    # what did happen here ?
    description = sqlalchemy.Column(sqlalchemy.String)

    def __repr__(self):
        return self.name


class Encounter(Base):
    """Model for the armor table"""
    __tablename__ = 'encounters'

    # incremental ID
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)

    adventure_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("adventures.id"))
    adventure = relationship("Adventure")

    # About the event
    name = sqlalchemy.Column(sqlalchemy.String)
    description = sqlalchemy.Column(sqlalchemy.String)

    # Who did fight ?
    players = sqlalchemy.Column(sqlalchemy.String)  # TODO this should be a list of character IDs where character.type == PC
    allies = sqlalchemy.Column(sqlalchemy.String)  # TODO this should be a list of character IDs
    opponents = sqlalchemy.Column(sqlalchemy.String)  # TODO this should be a list of character IDs

    def __repr__(self):
        return self.name


class Adventure(Base):
    """Model for the adventure table"""
    __tablename__ = 'adventures'

    # incremental ID
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)

    name = sqlalchemy.Column(sqlalchemy.String)
    description = sqlalchemy.Column(sqlalchemy.String)

    # History of this adventure
    events = sqlalchemy.Column(sqlalchemy.String)  # TODO this should be a list of events.id
    encounters = sqlalchemy.Column(sqlalchemy.String)  # TODO this should be a list of encounter.id
    #race_id = sqlalchemy.Column(Integer, sqlalchemy.ForeignKey("races.id"))
    #race = relationship("Race")

    players = sqlalchemy.Column(sqlalchemy.String)  # TODO this should be a list of players.id

    def __repr__(self):
        return self.name
