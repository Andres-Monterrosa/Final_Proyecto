from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import Libro
from django.urls import reverse_lazy
from .form import LibroForm

class LibroView(ListView):
    template_name = 'list_libro.html'
    model = Libro

class LibroCreate(CreateView):
    template_name = 'form.html'
    success_url = reverse_lazy('libro:libro_list')
    model = Libro
    form_class = LibroForm

class LibroUpdate(UpdateView):
    model = Libro
    template_name = 'form.html'
    success_url= reverse_lazy('libro:libro_list')
    form_class = LibroForm

class LibroDelete(DeleteView):
    model = Libro
    template_name = 'confirm.html'
    success_url = reverse_lazy('libro:libro_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['redirect'] = reverse_lazy('libro:libro_list')
        return context