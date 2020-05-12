from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from graphene_django.views import GraphQLView
from BGR.schema import schema
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('report.urls')),

    path(r'graphqlapi/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
