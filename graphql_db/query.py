import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField
from .object import User as User, Item as Item
from sql_app.models import User as UserModel, Item as ItemModel


class Query(graphene.ObjectType):
    node = relay.Node.Field()

    users = graphene.List(lambda: User, id=graphene.ID())

    def resolve_users(self, info, id=0):
        query = User.get_query(info)
        if id:
            query = query.filter(UserModel.id == id)
        return query.all()


    items = graphene.List(lambda: Item, id=graphene.ID())

    #items = SQLAlchemyConnectionField(Item)

    def resolve_items(self, info, id=0):
        query = Item.get_query(info)
        if id:
            query = query.filter(ItemModel.id == id)
        return query.all()
