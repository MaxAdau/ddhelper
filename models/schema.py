# coding: utf-8

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

from models.models import Event as EventModel
from models.models import EventActor as EventActorModel
from models.models import Actor as ActorModel


class Event(SQLAlchemyObjectType):
    """Represents the schema of Event Model"""
    class Meta:
        model = EventModel
        interfaces = (relay.Node, )


class EventActor(SQLAlchemyObjectType):
    """Represents the schema of EventActor Model"""
    class Meta:
        model = EventActorModel
        interfaces = (relay.Node, )


class Actor(SQLAlchemyObjectType):
    """Represents the schema of Actor Model"""
    class Meta:
        model = ActorModel
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    """Todo : need to check the capabilities of this one"""
    node = relay.Node.Field()

    all_event_actor = SQLAlchemyConnectionField(EventActor)
    all_actors = SQLAlchemyConnectionField(Actor)
    all_events = SQLAlchemyConnectionField(Event)

    actor_ = graphene.Field(Actor)

# Building my schema object
schema = graphene.Schema(query=Query, types=[Event, EventActor, Actor])