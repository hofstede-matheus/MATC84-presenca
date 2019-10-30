from django.urls import path
from presenca import views


urlpatterns = [
    path('', views.home, name='home'),
    path('materias/', views.MateriaListView.as_view(), name='materias'),
    path('materia/create/', views.MateriaCreate.as_view(), name='materia_create'),
    path('materia/<int:pk>/update/', views.MateriaUpdate.as_view(), name='materia_update'),
    path('materia/<int:pk>/delete/', views.MateriaDelete.as_view(), name='materia_delete'),    
]
