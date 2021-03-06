from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.main, name='main'),
    path('single/<int:pk>', views.single, name='single'),
    path('editor/', views.editor, name='editor'),
    path('data/', views.data, name='data'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
