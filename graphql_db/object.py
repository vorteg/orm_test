import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from sql_app.models import User as UserModel, Item as ItemModel

class User(SQLAlchemyObjectType):
   class Meta:
       model = UserModel
       interfaces = (relay.Node,)
       
class Item(SQLAlchemyObjectType):
   class Meta:
       model = ItemModel
       interfaces = (relay.Node,)
       

