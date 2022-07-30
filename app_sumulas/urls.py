from django.urls import path
from . views import SumulaListView, SumulaSingleView, MateriaSumulasView, TribunalSumulasView, \
    AddSumulasView, AddSumulaMateriaView, AddSumulaTribunalView, UpdateSumulaView, \
        DeleteSumulaView


urlpatterns = [
    path('', SumulaListView.as_view(), name='sumulas-list'),
    path('<int:pk>', SumulaSingleView.as_view(), name='sumula-single'),
    path('sumula_materia/<str:cats>/', MateriaSumulasView, name='sumula-materia'),
    path('sumula_tribunal/<str:cats>/', TribunalSumulasView, name='sumula-tribunal'),
    path('add_sumula/', AddSumulasView.as_view(), name='add-sumula'),
    path('add_sumula_materia/', AddSumulaMateriaView.as_view(), name='add-sumula-materia'),
    path('add_sumula_tribunal/', AddSumulaTribunalView.as_view(), name='add-sumula-tribunal'),
    path('article/edit/<int:pk>', UpdateSumulaView.as_view(), name='update-sumula'),
    path('article/<int:pk>/remove', DeleteSumulaView.as_view(), name='delete-sumula'),
    #path('images/', ImageView(), name = 'image-upload'),
]