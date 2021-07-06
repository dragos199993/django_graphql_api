import graphene
from graphene_django.debug import DjangoDebug

import blog.schema


class Query(
    blog.schema.Query,
    graphene.ObjectType,
):
    debug = graphene.Field(DjangoDebug, name='_debug')


class Mutation(
    blog.schema.Mutation,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
