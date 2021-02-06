from fastapi import FastAPI
#from models import db_session
from schema import schema
from starlette.graphql import GraphQLApp

app = FastAPI()
app.add_route("/", GraphQLApp(schema=schema))