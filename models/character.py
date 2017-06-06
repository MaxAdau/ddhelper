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

    # Race and class came from another model
    # http://docs.sqlalchemy.org/en/latest/orm/join_conditions.html
    race_id = Column(Integer, ForeignKey("races.id"))
    race = db.relationship("Race")
    klass_id = Column(Integer, ForeignKey("classes.id"))
    klass = db.relationship("Class")

    # TODO In order to handle the class / levels mechanics,
    #
    # I need a junction table like character_class:
    #   - character_id
    #   - class_id
    #   - level
    #   - order
    # Hit points

    current_hp = Column(Integer)
    total_hp = Column(Integer)

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
    AC = Column(Integer)  # TODO calculate it instead of hard code it ?
    AC_flatfooted = Column(Integer)
    AC_touch = Column(Integer)

    # Size and speed
    size = Column(String)  # TODO Take it from race.size ?
    initiative = Column(Integer)
    base_speed = Column(Integer)  # TODO Should be calculated from race.size

    # Saving throw
    SAVE_ref = Column(Integer)
    SAVE_for = Column(Integer)
    SAVE_will = Column(Integer)

    # Spells, Feats and skills
    spells = Column(String)  # todo handle a list of primary key
    feats = Column(String)  # todo handle a list of primary key
    skills = Column(String)  # todo handle a list of primary key

    # Weapons
    right_hand_id = Column(Integer, ForeignKey("weapons.id"))
    right_hand = db.relationship("Weapon", foreign_keys=[right_hand_id])

    left_hand_id = Column(Integer, ForeignKey("weapons.id"))
    left_hand = db.relationship("Weapon", foreign_keys=[left_hand_id])

    shield_id = Column(Integer, ForeignKey("armors.id"))  # todo handle the is_shield field
    shield = db.relationship("Armor", foreign_keys=[shield_id])

    # Armor
    armor_id = Column(Integer, ForeignKey("armors.id"))
    armor = db.relationship("Armor", foreign_keys=[armor_id])

    # Stuff # TODO change it to list os equipement type
    head_protection = Column(String)
    hand_protection = Column(String)
    inventory = Column(String)


