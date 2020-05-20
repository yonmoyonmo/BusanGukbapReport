import graphene
from graphene_django.types import DjangoObjectType
from report.models import Report2


class ReportType(DjangoObjectType):
    class Meta:
        model = Report2


class Query(object):
    all_reports = graphene.List(ReportType)

    def resolve_all_reports(self, info, **kwargs):
        return Report2.objects.all()
