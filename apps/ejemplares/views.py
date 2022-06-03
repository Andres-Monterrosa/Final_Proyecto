from django.shortcuts import render
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from .models import Ejemplares
from django.urls import reverse_lazy
from .form import EjemplarForm


# Create your views here.
class EjemplaresView(ListView):
    template_name = 'list.html'
    model = Ejemplares

class EjemplarCrear(CreateView):
    template_name = 'form.html'
    model = Ejemplares
    success_url = reverse_lazy('ejemplar:ejemplar_list')
    form_class = EjemplarForm

class EjemplarUpdate(UpdateView):
    model = Ejemplares
    template_name = 'form.html'
    success_url= reverse_lazy('ejemplar:ejemplar_list')
    form_class = EjemplarForm

class EjemplarDelete(DeleteView):
    model = Ejemplares
    template_name = 'confirm.html'
    success_url = reverse_lazy('ejemplar:ejemplar_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['redirect'] = reverse_lazy('ejemplar:ejemplar_list')
        return context