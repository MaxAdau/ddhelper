# coding: utf-8

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

from models.models import Event as EventModel
# from models.models import EventActor as EventActorModel
from models.models import Actor as ActorModel

from database import db_session

class Actor(SQLAlchemyObjectType):
    """Represents the schema of Actor Model"""
    class Meta:
        model = ActorModel
        interfaces = (relay.Node, )

class Event(SQLAlchemyObjectType):
    """
    An event located in a place with actors involved in it
    WHen done with it, I should handle the actors a proper way
    """
    class Meta:
        model = EventModel
        interfaces = (relay.Node, )

    present_actors = graphene.List(Actor)

    def resolve_present_actors(self, args, context, info):
        """All actors that were present in an event"""
        print('Context : {}\n Info : {}'.format(context, info))

        event_id = args.get('ID')
        print(event_id)
        # Use that http://docs.sqlalchemy.org/en/latest/orm/query.html#sqlalchemy.orm.query.Query.join

        # SQL request to handle this :
        # select events.name, events.description, actors.name from actors
        # left join event_actors on actors.id = event_actors.actor_id
        # left join events on events.id = event_actors.event_id where events.id = XX;

        # This return all actors
        # return db_session.query(ActorModel).\
        #     join(EventActorModel, ActorModel.id == EventActorModel.actor_id).\
        #     join(EventModel, EventModel.id == EventActorModel.event_id)

        # This return all actors
        # return db_session.query(ActorModel).\
        #     join(EventActorModel, ActorModel.id == EventActorModel.actor_id).\
        #     join(EventModel, EventModel.id == EventActorModel.event_id)


class Query(graphene.ObjectType):
    """Todo : need to check the capabilities of this one"""

    # From http://docs.graphene-python.org/en/latest/relay/nodes/ :
    # As is required in the Relay specification, the server must implement
    # a root field called node that returns a Node Interface.
    # For this reason, graphene provides the field relay.Node.Field,
    # which links to ANY type in the Schema which implements Node.
    node = relay.Node.Field()

    event = graphene.Field(Event, id=graphene.String())

    ##### For now, this do not work
    def resolve_event(self, args, context, info):

        # PROBLEM : This is the "graphene" id, not the postgre one
        event_id = args.get('id')

        event_query = Event.get_query(context) # SQLAlchemy query

        from graphql_relay.node.node import from_global_id

        print('event_id : {}'.format(event_id))

        local_id = from_global_id(event_id)
        print('local_id : {}'.format(local_id))

        # Get the original postgresql ID
        return event_query.get(local_id[1])

        # return query.get(id)

        # This do works
        # return db_session.query(EventModel)


    # actor = graphene.Field(Actor, id=graphene.ID())

    ##### For now, this do not work
    # def resolve_actor(self, args, context, info):
    #     query = Actor.get_query(context)
    #     id = args.get('id')
    #     return query.get(id)

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

    # all_actors = graphene.List(Actor)
    # @staticmethod
    # def resolve_all_actors(self, args, context, info):
    #     return db_session.query(ActorModel)
    #     # Use http://docs.sqlalchemy.org/en/latest/orm/query.html



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
