import graphene
import inventory.schema


class Queries(
    inventory.schema.Query,
    graphene.ObjectType
):
    dummy = graphene.String()


class Mutations(
    inventory.schema.Mutation,
    graphene.ObjectType,
):
    pass

schema = graphene.Schema(query=Queries, mutation=Mutations)