from django.urls import path
from . views import CasosListView, CasosSingleView, DireitoCasoView, MateriaCasoView, \
    AddCasosView, AddDireitoCasoView, AddMateriaCasoView, UpdatePostCasoView, DeletePostCasoView


urlpatterns = [
    path('', CasosListView.as_view(), name='casos-list'),
    path('<int:pk>', CasosSingleView.as_view(), name='caso-single'),
    path('direito/<str:cats>/', DireitoCasoView, name='direito-caso'),
    path('materia/<str:cats>/', MateriaCasoView, name='materia-caso'),
    path('add_casos/', AddCasosView.as_view(), name='add_casos'),
    path('add_direito_caso/', AddDireitoCasoView.as_view(), name='add_direito_caso'),
    path('add_materia_caso/', AddMateriaCasoView.as_view(), name='add_materia_caso'),
    path('article/edit/<int:pk>', UpdatePostCasoView.as_view(), name='update_caso'),
    path('article/<int:pk>/remove', DeletePostCasoView.as_view(), name='delete_caso'),
    #path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    #path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    #path('images/', ImageView(), name = 'image-upload'),
]
