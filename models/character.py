# coding: utf-8

from sqlalchemy import Column, Integer, String, ForeignKey, Float

from models.models import db, BaseModel

class Character(BaseModel, db.Model):
    """Model for the character table"""
    __tablename__ = 'chars'

    # Incremental ID
    id = Column(Integer, primary_key=True)

    # About the character
    player_name = Column(String)
    name = Column(String)
    age = Column(Integer)
    level = Column(Integer)
    description = Column(String)

    # Race and class cames from another model
    # http://docs.sqlalchemy.org/en/latest/orm/join_conditions.html
    race_id = Column(Integer, ForeignKey("races.id"))
    race = db.relationship("Race")
    klass_id = Column(Integer, ForeignKey("classes.id"))
    klass = db.relationship("Class")

    # Character carac
    # TODO put it in a custom type
    str = Column(Integer)
    dex = Column(Integer)
    con = Column(Integer)
    int = Column(Integer)
    wis = Column(Integer)
    cha = Column(Integer)

    # Base attack Bonus
    BAB = Column(Integer)

    # Armor Class
    AC_natural = Column(Integer)
    magic_resist = Column(Integer)
    # TODO calculate it instead of hard code it
    AC = Column(Integer)
    AC_flatfooted = Column(Integer)
    AC_touch = Column(Integer)

    # Size and speed
    size = Column(String) # TODO Take it from race.size
    initiative = Column(Integer)

    # TODO Should be calculated
    speed = Column(Integer)

    # Saving throw
    SAVE_ref = Column(Integer)
    SAVE_for = Column(Integer)
    SAVE_will = Column(Integer)

    # Weapons # TODO Change type to weapon type
    right_hand_1 = Column(String)
    left_hand_1 = Column(String)
    right_hand_2 = Column(String)
    left_hand_2 = Column(String)


    # Armor # TODO Change type armor/shield type
    armor = Column(String)
    shield = Column(String)

    # Stuff # TODO change it to list os equipement type
    head_protection = Column(String)
    hand_protection = Column(String)
