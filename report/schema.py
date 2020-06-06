import graphene
from graphene_django.types import DjangoObjectType
from report.models import *


class Report3Type(DjangoObjectType):
    class Meta:
        model = Report3


class ReportImagesType(DjangoObjectType):
    class Meta:
        model = ReportImages


class GukmoolType(DjangoObjectType):
    class Meta:
        model = Gukmool


class GoguiType(DjangoObjectType):
    class Meta:
        model = Gogui


class KimchiType(DjangoObjectType):
    class Meta:
        model = Kimchi


class ServiceType(DjangoObjectType):
    class Meta:
        model = Service


class WeesaengType(DjangoObjectType):
    class Meta:
        model = Weesaeng


class LatlngType(DjangoObjectType):
    class Meta:
        model = Latlng


class Query(object):
    all_reports = graphene.List(Report3Type)
    all_images = graphene.List(ReportImagesType)
    all_gukmools = graphene.List(GukmoolType)
    all_goguis = graphene.List(GoguiType)
    all_kimchis = graphene.List(KimchiType)
    all_services = graphene.List(ServiceType)
    all_weesaengs = graphene.List(WeesaengType)
    all_Latlng = graphene.List(LatlngType)

    def resolve_all_reports(self, info, **kwargs):
        return Report3.objects.all()

    def resolve_all_images(self, info, **kwargs):
        return ReportImages.objects.all()

    def resolve_all_gukmools(self, info, **kwargs):
        return Gukmool.objects.all()

    def resolve_all_goguis(self, info, **kwargs):
        return Gogui.objects.all()

    def resolve_all_kimchis(self, info, **kwargs):
        return Kimchi.objects.all()

    def resolve_all_services(self, info, **kwargs):
        return Service.objects.all()

    def resolve_all_weesaengs(self, info, **kwargs):
        return Weesaeng.objects.all()

    def resolve_all_Latlngs(self, info, **kwargs):
        return Latlng.objects.all()
