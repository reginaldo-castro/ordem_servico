from django.contrib import admin
from django.urls import path, include
from ninja import NinjaAPI

from .api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.core.urls', namespace='core')),
    path('crm/', include('backend.crm.urls', namespace='crm')),
    path('servico/', include('backend.servico.urls', namespace='servico')),
    path('api/v1/', api.urls),
]
