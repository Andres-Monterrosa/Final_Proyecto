from django.urls import path
from .views import *

app_name = 'ejemplar'

urlpatterns = [
    path('', EjemplaresView.as_view(),name='ejemplar_list'),
    path('crear/',EjemplarCrear.as_view(),name='ejemplar_crear'),
    path('update/<int:pk>',EjemplarUpdate.as_view(),name='ejemplar_update'),
    path('delete/<int:pk>',EjemplarDelete.as_view(),name='ejemplar_delete'),    
]
