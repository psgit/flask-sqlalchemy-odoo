import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import db_session, Bank as BankModel, Company as CompanyModel, Partner as PartnerModel, User as UserModel

class Bank(SQLAlchemyObjectType):
    class Meta:
        model = BankModel
        interfaces = (relay.Node, )


class BankConnection(relay.Connection):
    class Meta:
        node = Bank

class Company(SQLAlchemyObjectType):
    class Meta:
        model = CompanyModel
        interfaces = (relay.Node, )

class CompanyConnection(relay.Connection):
    class Meta:
        node = Company

class Partner(SQLAlchemyObjectType):
    class Meta:
        model = PartnerModel
        interfaces = (relay.Node, )


class PartnerConnection(relay.Connection):
    class Meta:
        node = Partner

class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node, )


class UserConnection(relay.Connection):
    class Meta:
        node = User


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_users = SQLAlchemyConnectionField(User._meta.connection)
    all_banks = SQLAlchemyConnectionField(Bank._meta.connection)
    all_companies = SQLAlchemyConnectionField(Company._meta.connection)
    all_partners = SQLAlchemyConnectionField(Partner._meta.connection)

schema = graphene.Schema(query=Query)