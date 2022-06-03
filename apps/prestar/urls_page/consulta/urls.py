from django.urls import path
from ...views.consulta.views import *

urlpatterns = [
    path('',Consultas.as_view(),name='consultas')
]
