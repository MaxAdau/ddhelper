# coding: utf-8

import graphene
from graphene import relay
from graphql_relay.node.node import from_global_id
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

from models.models import Event as EventModel
from models.models import EventActor as EventActorModel
from models.models import Actor as ActorModel
from models.models import Location as LocationModel

from database import db_session


class Location(SQLAlchemyObjectType):
    """A location, where things happens"""
    class Meta:
        model = LocationModel
        interfaces = (relay.Node, )


class Actor(SQLAlchemyObjectType):
    """An actor, could be a PC or NPC"""
    class Meta:
        model = ActorModel
        interfaces = (relay.Node, )


class Event(SQLAlchemyObjectType):
    """
    An dated event, located in a certain location, possibly involving actor
    """
    class Meta:
        model = EventModel
        interfaces = (relay.Node, )

    present_actors = graphene.List(Actor)
    location = graphene.Field(Location)

    def resolve_present_actors(self, args, context, info):
        """All actors that were present in an event"""

        # This is as easy as that :
        # https://github.com/graphql-python/graphene/issues/378
        parent_event_id = self.id

        # Using that http://docs.sqlalchemy.org/en/latest/orm/query.html#sqlalchemy.orm.query.Query.join
        # Returns all actors linked to an Event, using EventActors table
        return db_session.query(ActorModel).\
            join(EventActorModel, ActorModel.id == EventActorModel.actor_id).\
            join(EventModel, EventModel.id == EventActorModel.event_id).\
            filter(EventModel.id == parent_event_id)

    # def resolve_location(self, args, context, info):
    #     """Location linked to an event"""
    #     return db_session(LocationModel).\
    #         join()

class Query(graphene.ObjectType):
    """Todo : need to check the capabilities of this one"""

    # From http://docs.graphene-python.org/en/latest/relay/nodes/ :
    # As is required in the Relay specification, the server must implement
    # a root field called node that returns a Node Interface.
    # For this reason, graphene provides the field relay.Node.Field,
    # which links to ANY type in the Schema which implements Node.
    node = relay.Node.Field()

    # Schema queries
    event = graphene.Field(Event, id=graphene.String())

    all_events = SQLAlchemyConnectionField(Event)

    actor = graphene.Field(Actor)
    location = graphene.Field(Location)

    # Queries resolvers
    @staticmethod
    def resolve_event(self, args, context, info):
        """Get an event, need an ID"""
        event_id = args.get('id')
        # SQLAlchemy query
        event_query = Event.get_query(context)
        # Get the original postgresql ID
        local_id = from_global_id(event_id)[1]
        return event_query.get(local_id)

    @staticmethod
    def resolve_all_events(self, *args, **kwargs):
        return db_session.query(EventModel)

# Building my schema object
schema = graphene.Schema(query=Query, types=[Event, Actor])

# TODO : What to do with it ?
default_query = '''
 allEvents (first :1){
    edges {
      cursor
      node {
        id
        name
        presentActors {
          name
        }
      }
    }
  }
'''