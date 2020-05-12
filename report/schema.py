import graphene
from graphene_django.types import DjangoObjectType
from report.models import Report


class ReportType(DjangoObjectType):
    class Meta:
        model = Report


class Query(object):
    all_reports = graphene.List(ReportType)

    def resolve_all_reports(self, info, **kwargs):
        return Report.objects.all()
