# coding: utf-8

import sqlalchemy as sa
from sqlalchemy.orm import backref, relationship

from database import Base


class Event(Base):
    """Model for the armor table"""
    __tablename__ = 'events'

    # incremental ID
    id = sa.Column(sa.Integer, primary_key=True)

    # About the event
    name = sa.Column(sa.String)

    # What did happen here ?
    description = sa.Column(sa.String)

    # TODO ADD DATE
    def __repr__(self):
        return self.name


class EventActor(Base):
    """Relation between events and actors"""
    __tablename__ = 'event_actors'

    # incremental ID
    id = sa.Column(sa.Integer, primary_key=True)

    # actor relation
    actor_id = sa.Column(sa.Integer, sa.ForeignKey("actors.id"))
    actor = relationship("Actor")

    # event relation
    event_id = sa.Column(sa.Integer, sa.ForeignKey("events.id"))
    event = relationship("Event")

    def __repr__(self):
        return self.id


class Actor(Base):
    __tablename__ = 'actors'

    # incremental ID
    id = sa.Column(sa.Integer, primary_key=True)

    # Later, this will be a user
    name = sa.Column(sa.String)

    def __repr__(self):
        return self.name




'''
class EventActor(Base):
    """Model representing actors of an event"""
    __tablename__ = 'eventactors'

    # Incremental ID
    id = sa.Column(sa.Integer, primary_key=True)

    event_id = sa.Column(sa.Integer, sa.ForeignKey("events.id"))
    adventure = relationship("Event")
'''


'''
# TODO add all fields of this class, matching postgresql
class Race(Base):
    """Model for the race table"""
    __tablename__ = 'races'

    # incremental ID
    id = sa.Column(sa.Integer, primary_key=True)

    # About the race
    name = sa.Column(sa.String)
    description = sa.Column(sa.String)

    # TODO move it to an ENUM type
    size = sa.Column(sa.String)

    def __repr__(self):
        return self.name


class Klass(Base):
    __tablename__ = 'klasses'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    description = sa.Column(sa.String)
    hp = sa.Column(sa.Integer)

    def __repr__(self):
        return self.name


class Character(Base):
    __tablename__ = 'chars'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)

    race_id = sa.Column(sa.Integer, sa.ForeignKey('races.id'))
    klass_id = sa.Column(sa.Integer, sa.ForeignKey('klasses.id'))
    race = relationship(Race)
    klass_ = relationship(Klass)

class Weapon(Base):
    """Model for the weapon table"""
    __tablename__ = 'weapons'

    # incremental ID
    id = sa.Column(sa.Integer, primary_key=True)

    # About the weapon
    name = sa.Column(sa.String)
    description = sa.Column(sa.String)

    # Damage
    dmg_S = sa.Column(sa.String)
    dmg_M = sa.Column(sa.String)
    critical = sa.Column(sa.String)
    range_increment = sa.Column(sa.Integer) # in meter

    # Other
    weight = sa.Column(sa.Float) # in Kilo
    dmg_type = sa.Column(sa.String)
    cost = sa.Column(sa.String) # in GP

    def __repr__(self):
        return self.name

class Armor(Base):
    """Model for the armor table"""
    __tablename__ = 'armors'

    # incremental ID
    id = sa.Column(sa.Integer, primary_key=True)

    # Is this armor a shield ?
    is_shield = sa.Column(sa.Boolean)

    # About the armor
    name = sa.Column(sa.String)
    description = sa.Column(sa.String)

    # Damage
    ca_bonus = sa.Column(sa.Integer)
    max_dex = sa.Column(sa.Integer)
    armor_penalty_check = sa.Column(sa.Integer)
    arcane_spell_fail = sa.Column(sa.Integer)
    speed_6m = sa.Column(sa.Integer)
    speed_9m = sa.Column(sa.Integer)

    # Other
    weight = sa.Column(sa.Float)  # in Kilo
    dmg_type = sa.Column(sa.String)
    cost = sa.Column(sa.String)  # in GP

    def __repr__(self):
        return self.name


class Encounter(Base):
    """Model for the armor table"""
    __tablename__ = 'encounters'

    # incremental ID
    id = sa.Column(sa.Integer, primary_key=True)

    adventure_id = sa.Column(sa.Integer, sa.ForeignKey("adventures.id"))
    adventure = relationship("Adventure")

    # About the event
    name = sa.Column(sa.String)
    description = sa.Column(sa.String)

    # Who did fight ?
    players = sa.Column(sa.String)
    # TODO this should be a list of character IDs where character.type == PC

    allies = sa.Column(sa.String)
    # TODO this should be a list of character IDs

    opponents = sa.Column(sa.String)
    # TODO this should be a list of character IDs

    def __repr__(self):
        return self.name


class Adventure(Base):
    """Model for the adventure table"""
    __tablename__ = 'adventures'

    # incremental ID
    id = sa.Column(sa.Integer, primary_key=True)

    name = sa.Column(sa.String)
    description = sa.Column(sa.String)

    # History of this adventure
    events = sa.Column(sa.String)  # TODO this should be a list of events.id
    encounters = sa.Column(sa.String)  # TODO this should be a list of encounter.id

    players = sa.Column(sa.String)  # TODO this should be a list of players.id

    def __repr__(self):
        return self.name
'''