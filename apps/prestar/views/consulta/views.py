from django.db.models import Count
from django.views.generic import TemplateView
from django.shortcuts import render
from apps.prestar.models import Prestar

class Consultas(TemplateView):
    template_name = 'consulta/consulta.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        fechai = request.POST['fechai']
        fechaf = request.POST['fechaf']
        consulta = request.POST['consulta_type']
        value = {}
        if consulta == '1':
            value = Prestar.objects.values('ejemplares__codigo_libro__titulo','fecha_pres','fecha_dev','usuarios__nombre').filter(fecha_pres__range=[fechai,fechaf])[0]
        elif consulta == '2':
            value = Prestar.objects.values('ejemplares__codigo_libro__titulo').filter(fecha_pres__range=[fechai,fechaf]).annotate(total=Count('ejemplares__codigo_libro__titulo'))
        elif consulta == '3':
            value = Prestar.objects.values('usuarios__nombre').filter(fecha_pres__range=[fechai,fechaf]).annotate(total=Count('usuarios__nombre'))

        context['response'] = value
        return render(request,'consulta/consulta.html',context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context