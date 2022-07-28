from pyexpat import model
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import CasoConcreto, MateriaCaso, DireitoCaso
from .forms import AddCasoForm, AddDireitoCasoForm, AddMateriaCasoForm, EditCasoForm
from django.urls import reverse_lazy


class CasosListView(ListView):
    model = CasoConcreto
    template_name = 'templates_casos/casos_list.html'
    ordering = ['-data']

    def get_context_data(self, *args, **kwargs):
        cat_menu_materia_caso = MateriaCaso.objects.all()
        context = super(CasosListView, self).get_context_data(*args, **kwargs)
        context["cat_menu_materia_caso"] = cat_menu_materia_caso
        return context

    def get_context_data(self, *args, **kwargs):
        cat_menu_direito_caso = DireitoCaso.objects.all()
        context = super(CasosListView, self).get_context_data(*args, **kwargs)
        context["cat_menu_direito_caso"] = cat_menu_direito_caso
        return context


def MateriaCasoView(request, cats):
    materia_caso_casos = CasoConcreto.objects.filter(materia_caso=cats)
    return render(request, 'templates_casos/materia_caso.html', {'cats': cats.title(), 'materia_caso_casos': materia_caso_casos})


def DireitoCasoView(request, cats):
    direito_caso_casos = CasoConcreto.objects.filter(direito_caso=cats)
    return render(request, 'templates_casos/direito_caso.html', {'cats': cats.title(), 'direito_caso_casos': direito_caso_casos})


class CasosSingleView(DetailView):
    model = CasoConcreto
    template_name = 'templates_casos/caso_single.html'



class AddCasosView(CreateView):
    model = CasoConcreto
    form_class = AddCasoForm
    template_name = 'templates_casos/add_casos.html'


class AddDireitoCasoView(CreateView):
    model = DireitoCaso
    form_class = AddDireitoCasoForm
    template_name = 'templates_casos/add_direito_caso.html'


class AddMateriaCasoView(CreateView):
    model = MateriaCaso
    form_class = AddMateriaCasoForm
    template_name = 'templates_casos/add_materia_caso.html'


class UpdatePostCasoView(UpdateView):
    model = CasoConcreto
    form_class = EditCasoForm
    template_name = 'templates_casos/update_caso.html'
    success_url = reverse_lazy('home')


class DeletePostCasoView(DeleteView):
    model = CasoConcreto
    template_name = 'templates_casos/delete_caso.html'
    success_url = reverse_lazy('home')
