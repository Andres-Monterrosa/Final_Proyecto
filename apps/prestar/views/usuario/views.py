from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from ...models import Usuarios
from django.urls import reverse_lazy
from ...form import UsuarioForm

class UsuarioView(ListView):
    template_name = 'usuario/list.html'
    model = Usuarios

class UsuarioCreate(CreateView):
    template_name = 'form.html'
    success_url = reverse_lazy('prestar:usuario_list')
    model = Usuarios
    form_class = UsuarioForm

class UsuarioUpdate(UpdateView):
    model = Usuarios
    template_name = 'form.html'
    success_url= reverse_lazy('prestar:usuario_list')
    form_class = UsuarioForm

class UsuarioDelete(DeleteView):
    model = Usuarios
    template_name = 'confirm.html'
    success_url = reverse_lazy('prestar:usuario_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['redirect'] = reverse_lazy('prestar:usuario_list')
        return context