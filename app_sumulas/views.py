from pyexpat import model
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Sumulas, SumulaMateria, SumulaTribunal
from .forms import AddSumulaForm, AddSumulaMateriaForm, AddSumulaTribunalForm, EditSumulaForm
from django.urls import reverse_lazy


class SumulaListView(ListView):
    model = Sumulas
    template_name = 'templates_sumulas/sumulas_list.html'
    ordering = ['-data']

    def get_context_data(self, *args, **kwargs):
        cat_menu_sumula_materia = SumulaMateria.objects.all()
        context = super(SumulaListView, self).get_context_data(*args, **kwargs)
        context["cat_menu_sumula_materia"] = cat_menu_sumula_materia
        return context

    def get_context_data(self, *args, **kwargs):
        cat_menu_sumula_tribunal = SumulaTribunal.objects.all()
        context = super(SumulaListView, self).get_context_data(*args, **kwargs)
        context["cat_menu_sumula_tribunal"] = cat_menu_sumula_tribunal
        return context


def MateriaSumulasView(request, cats):
    materia_sumula_sumulas = Sumulas.objects.filter(sumula_materia=cats)
    return render(
        request, 'templates_sumulas/sumula_materia.html', {
            'cats': cats.title(), 'materia_sumula_sumulas': materia_sumula_sumulas})


def TribunalSumulasView(request, cats):
    tribunal_sumula_sumulas = Sumulas.objects.filter(sumula_tribunal=cats)
    return render(
        request, 'templates_sumulas/sumula_tribunal.html', {
            'cats': cats.title(), 'tribunal_sumula_sumulas': tribunal_sumula_sumulas})


class SumulaSingleView(DetailView):
    model = Sumulas
    template_name = 'templates_sumulas/sumula_single.html'


class AddSumulasView(CreateView):
    model = Sumulas
    form_class = AddSumulaForm
    template_name = 'templates_sumulas/add_sumula.html'


class AddSumulaMateriaView(CreateView):
    model = SumulaMateria
    form_class = AddSumulaMateriaForm
    template_name = 'templates_sumulas/add_sumula_materia.html'


class AddSumulaTribunalView(CreateView):
    model = SumulaTribunal
    form_class = AddSumulaTribunalForm
    template_name = 'templates_sumulas/add_sumula_tribunal.html'


class UpdateSumulaView(UpdateView):
    model = Sumulas
    form_class = EditSumulaForm
    template_name = 'templates_sumulas/update_sumula.html'
    success_url = reverse_lazy('home')


class DeleteSumulaView(DeleteView):
    model = Sumulas
    template_name = 'templates_sumulas/delete_sumula.html'
    success_url = reverse_lazy('home')

