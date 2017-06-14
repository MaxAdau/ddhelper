import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from models.models import Race as RaceModel
from models.models import Character as CharacterModel
from models.models import Class as ClassModel


class Race(SQLAlchemyObjectType):

    class Meta:
        model = RaceModel
        interfaces = (relay.Node, )


class Character(SQLAlchemyObjectType):

    class Meta:
        model = CharacterModel
        interfaces = (relay.Node, )

class Class(SQLAlchemyObjectType):

    class Meta:
        model = ClassModel
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_characters = SQLAlchemyConnectionField(Character)
    all_classes = SQLAlchemyConnectionField(Class)
    all_races = SQLAlchemyConnectionField(Race)

    class_ = graphene.Field(Class)



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

schema = graphene.Schema(query=Query, types=[Race, Character, Class])
