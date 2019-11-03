from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

from presenca.models import Professor, Aluno, Materia, Turma, Presenca

def home(request):

    context = {

    }

    # Render the HTML template home.html with the data in the context variable
    return render(request, 'home.html', context=context)


from presenca.models import Materia
from django.views import generic

class MateriaListView(generic.ListView):
    model = Materia

class MateriaCreate(CreateView):
    model = Materia
    fields = '__all__'
    success_url = reverse_lazy('materias')

class MateriaUpdate(UpdateView):
    model = Materia
    fields = '__all__'
    success_url = reverse_lazy('materias')

class MateriaDelete(DeleteView):
    model = Materia
    success_url = reverse_lazy('materias')
