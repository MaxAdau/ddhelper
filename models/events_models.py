# coding: utf-8

import sqlalchemy
from sqlalchemy.orm import relationship

from database import Base

class Event(Base):
    # TODO NOW : I want colin to be able to graphql those events
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

    # TODO ADD DATE
    def __repr__(self):
        return self.name

class EventActor(Base):
    """Model representing actors of an event"""
    __tablename__ = 'eventactors'

    # Incremental ID
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)

    event_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("events.id"))
    adventure = relationship("Event")