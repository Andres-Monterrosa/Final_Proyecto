from django.urls import path
from ...views.usuario.views import *

urlpatterns = [
    path('',UsuarioView.as_view(),name='usuario_list'),
    path('crear/',UsuarioCreate.as_view(),name='usuario_crear'),
    path('update/<int:pk>',UsuarioUpdate.as_view(),name='usuario_update'),
    path('delete/<int:pk>',UsuarioDelete.as_view(),name='usuario_delete'),

]
