# coding: utf-8

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


class Events(BaseModel, db.Model):
    """Model for the armor table"""
    __tablename__ = 'events'

    # incremental ID
    id = Column(Integer, primary_key=True)

    # Is this armor a shield ?
    name = Column(String)

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
