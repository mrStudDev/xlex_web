from django.urls import path
from . views import QuestionsListView, QuestionSingleView, MateriaQuestionView, BancaQuestionView, \
    AddQuestionsView, AddMateriaQuestionView, AddBancaQuestionView, UpdateQuestionView, DeleteQuestionView, \
        RespostaQuestionView


urlpatterns = [
    path('', QuestionsListView.as_view(), name='questions-list'),
    path('<int:pk>', QuestionSingleView.as_view(), name='question-single'),
    path('materia_question/<str:cats>/', MateriaQuestionView, name='materia-question'),
    path('banca_question/<str:cats>/', BancaQuestionView, name='banca-question'),
    path('add_questions/', AddQuestionsView.as_view(), name='add_questions'),
    path('resposta/<int:pk>', RespostaQuestionView.as_view(), name='resposta-question'),
    path('add_materia_question/', AddMateriaQuestionView.as_view(), name='add_materia_question'),
    path('add_banca_question/', AddBancaQuestionView.as_view(), name='add_banca_question'),
    path('article/edit/<int:pk>', UpdateQuestionView.as_view(), name='update-question'),
    path('article/<int:pk>/remove', DeleteQuestionView.as_view(), name='delete-question'),
]
