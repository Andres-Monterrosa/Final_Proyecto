from django.urls import path
from .views import *

app_name = 'libro'

urlpatterns = [
    path('', LibroView.as_view(),name='libro_list'),
    path('crear/',LibroCreate.as_view(),name='libro_crear'),
    path('update/<int:pk>',LibroUpdate.as_view(),name='libro_udpate'),
    path('delete/<int:pk>',LibroDelete.as_view(),name='libro_delete'),
]
