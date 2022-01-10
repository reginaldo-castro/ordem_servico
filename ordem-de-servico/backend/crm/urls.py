from django.urls import path
from backend.crm import views as v

app_name = 'crm'

urlpatterns = [
    path('', v.ClienteListView.as_view(), name='cliente_list'),
]