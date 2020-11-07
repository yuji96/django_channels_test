import graphene
import chat.schema


class Query(chat.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(
    query=Query,
)
