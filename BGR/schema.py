import graphene
import report.schema


class Query(report.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
