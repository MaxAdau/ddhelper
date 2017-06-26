# coding: utf-8

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

from models.models import Event as EventModel
from models.models import EventActor as EventActorModel
from models.models import Actor as ActorModel

from database import db_session


class EventActor(SQLAlchemyObjectType):
    """Represents the schema of EventActor Model"""
    class Meta:
        model = EventActorModel
        interfaces = (relay.Node, )


class Event(SQLAlchemyObjectType):
    """Represents the schema of Event Model"""
    class Meta:
        model = EventModel
        interfaces = (relay.Node, )

    def get_node(self, *args, **kwargs):
        return db_session.query(EventModel).first()

class Actor(SQLAlchemyObjectType):
    """Represents the schema of Actor Model"""
    class Meta:
        model = ActorModel
        interfaces = (relay.Node, )

    def get_node(self, args, context, info):
        return '{} {}'. format(context, info)

class Query(graphene.ObjectType):
    """Todo : need to check the capabilities of this one"""

    # From http://docs.graphene-python.org/en/latest/relay/nodes/ :
    # As is required in the Relay specification, the server must implement
    # a root field called node that returns a Node Interface.
    # For this reason, graphene provides the field relay.Node.Field,
    # which links to ANY type in the Schema which implements Node.
    node = relay.Node.Field()

    event = graphene.Field(Event, id=graphene.ID())

    ##### For now, this do not work
    def resolve_event(self, args, context, info):
        query = Event.get_query(context)
        id = args.get('id')
        return query.get(id)

    actor = graphene.Field(Actor, id=graphene.ID())

    ##### For now, this do not work
    def resolve_actor(self, args, context, info):
        query = Actor.get_query(context)
        id = args.get('id')
        return query.get(id)

    # event = relay.Node.Field(Event)
    # event = graphene.Field(Event)
    #
    # @staticmethod
    # def resolve_event(self, *args, **kwargs):
    #     return db_session.query(EventModel).first()

    # This works well
    all_events = graphene.List(Event)
    @staticmethod
    def resolve_all_events(self, *args, **kwargs):
        return db_session.query(EventModel)
        # Use http://docs.sqlalchemy.org/en/latest/orm/query.html

    all_actors = graphene.List(Actor)
    @staticmethod
    def resolve_all_actors(self, args, context, info):
        return db_session.query(ActorModel)
        # Use http://docs.sqlalchemy.org/en/latest/orm/query.html



    # What do that do ?
    # all_actors = SQLAlchemyConnectionField(Actor)
    # all_events = SQLAlchemyConnectionField(Event)

    actor = graphene.Field(Actor)

    #all_actors = graphene.List(Actor)

    #actor = graphene.Field(Actor)




    # @staticmethod
    # def resolve_actor(self, *args, **kwargs):
    #     return db_session.query(ActorModel).first()
    #
    # @staticmethod
    # def resolve_actors(self, *args, **kwargs):
    #     return db_session.query(ActorModel).all()

# Building my schema object
schema = graphene.Schema(query=Query, types=[Event, Actor])
