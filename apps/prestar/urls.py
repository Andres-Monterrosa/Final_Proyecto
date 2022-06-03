from django.urls import path,include

app_name = 'prestar'

urlpatterns = [
    path('prestar/',include('apps.prestar.urls_page.prestar.urls')),
    path('usuarios/',include('apps.prestar.urls_page.usuario.urls')),
    path('consulta/',include('apps.prestar.urls_page.consulta.urls'))
]
