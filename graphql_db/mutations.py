import graphene

from  sql_app import database
from  .object import User as User, Item as Item
from sql_app.models import User as UserModel, Item as ItemModel


class UserMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
       # hashedPassword = graphene.String()
        #isActive = graphene.Boolean(required=True)
        
    user = graphene.Field(lambda: User)
    
    def mutate(self, info, email):
        user = UserModel(email=email)
        database.SessionLocal.add(user)
        database.SessionLocal.commit()
        
        return UserMutation(user=user)
    
class Mutation(graphene.ObjectType):
   mutate_user = UserMutation.Field()