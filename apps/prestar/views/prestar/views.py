from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from ...models import Prestar
from django.urls import reverse_lazy
from ...form import PrestarForm

class PrestarView(ListView):
    template_name = 'list_prestar.html'
    model = Prestar

class PrestarCreate(CreateView):
    template_name = 'form.html'
    success_url = reverse_lazy('prestar:prestar_list')
    model = Prestar
    form_class = PrestarForm

class PrestarUpdate(UpdateView):
    model = Prestar
    template_name = 'form.html'
    success_url= reverse_lazy('prestar:prestar_list')
    form_class = PrestarForm

class PrestarDelete(DeleteView):
    model = Prestar
    template_name = 'confirm.html'
    success_url = reverse_lazy('prestar:prestar_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['redirect'] = reverse_lazy('prestar:prestar_list')
        return context