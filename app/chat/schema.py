import graphene
from graphene_django import DjangoObjectType

import chat.models


class Message(DjangoObjectType):
    class Meta:
        model = chat.models.Message


class Query(graphene.ObjectType):
    messages = graphene.List(Message)
