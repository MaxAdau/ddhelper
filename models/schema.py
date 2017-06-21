import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from models.models import Event as EventModel
from models.models import EventActor as EventActorModel
from models.models import Actor as ActorModel


class Event(SQLAlchemyObjectType):
    class Meta:
        model = EventModel
        interfaces = (relay.Node, )


class EventActor(SQLAlchemyObjectType):
    class Meta:
        model = EventActorModel
        interfaces = (relay.Node, )

class Actor(SQLAlchemyObjectType):
    class Meta:
        model = ActorModel
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_th = SQLAlchemyConnectionField(EventActor)
    all_classes = SQLAlchemyConnectionField(Actor)
    all_events = SQLAlchemyConnectionField(Event)

    class_ = graphene.Field(Actor)


'''
class Department(SQLAlchemyObjectType):

    class Meta:
        model = DepartmentModel
        interfaces = (relay.Node, )


class Employee(SQLAlchemyObjectType):

    class Meta:
        model = EmployeeModel
        interfaces = (relay.Node, )


class Role(SQLAlchemyObjectType):

    class Meta:
        model = RoleModel
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_employees = SQLAlchemyConnectionField(Employee)
    all_roles = SQLAlchemyConnectionField(Role)
    role = graphene.Field(Role)
'''

schema = graphene.Schema(query=Query, types=[Event, EventActor, Actor])
