from django.urls import path
from ...views.prestar.views import *

urlpatterns = [
    path('',PrestarView.as_view(),name='prestar_list'),
    path('crear/',PrestarCreate.as_view(),name='prestar_crear'),
    path('update/<int:pk>',PrestarUpdate.as_view(),name='prestar_update'),
    path('delete/<int:pk>',PrestarDelete.as_view(),name='prestar_delete'),
]
