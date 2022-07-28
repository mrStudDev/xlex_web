from pyexpat import model
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Question, MateriaQuestion, BancaQuestion
from .forms import AddQuestionForm, AddMateriaQuestionForm, AddBancaQuestionForm, EditQuestionForm
from django.urls import reverse_lazy


class QuestionsListView(ListView):
    model = Question
    template_name = 'templates_questions/questions_list.html'
    ordering = ['-data']

    def get_context_data(self, *args, **kwargs):
        cat_menu_materia_question = MateriaQuestion.objects.all()
        context = super(QuestionsListView, self).get_context_data(*args, **kwargs)
        context["cat_menu_materia_question"] = cat_menu_materia_question
        return context

    def get_context_data(self, *args, **kwargs):
        cat_menu_banca_question = BancaQuestion.objects.all()
        context = super(QuestionsListView, self).get_context_data(*args, **kwargs)
        context["cat_menu_banca_question"] = cat_menu_banca_question
        return context


def MateriaQuestionView(request, cats):
    materia_question_questions = Question.objects.filter(materia_question=cats)
    return render(request, 'templates_questions/materia_question.html', {'cats': cats.title(), 'materia_question_questions': materia_question_questions})


def BancaQuestionView(request, cats):
    banca_question_questions = Question.objects.filter(banca_question=cats)
    return render(request, 'templates_questions/banca_question.html', {'cats': cats.title(), 'banca_question_questions': banca_question_questions})


class QuestionSingleView(DetailView):
    model = Question
    template_name = 'templates_questions/question_single.html'


class RespostaQuestionView(DeleteView):
    model = Question
    template_name = 'templates_questions/resposta_question.html'


class AddQuestionsView(CreateView):
    model = Question
    form_class = AddQuestionForm
    template_name = 'templates_questions/add_questions.html'


class AddMateriaQuestionView(CreateView):
    model = MateriaQuestion
    form_class = AddMateriaQuestionForm
    template_name = 'templates_questions/add_materia_question.html'


class AddBancaQuestionView(CreateView):
    model = BancaQuestion
    form_class = AddBancaQuestionForm
    template_name = 'templates_questions/add_banca_question.html'


class UpdateQuestionView(UpdateView):
    model = Question
    form_class = EditQuestionForm
    template_name = 'templates_questions/update_question.html'
    success_url = reverse_lazy('home')


class DeleteQuestionView(DeleteView):
    model = Question
    template_name = 'templates_questions/delete_question.html'
    success_url = reverse_lazy('home')

