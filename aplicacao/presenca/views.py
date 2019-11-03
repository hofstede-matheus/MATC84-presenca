from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

from django.contrib.auth.decorators import login_required
from presenca.models import Professor, Aluno, Materia, Turma, Presenca

@login_required
def home(request):

    context = {

    }

    # Render the HTML template home.html with the data in the context variable
    return render(request, 'home.html', context=context)


from presenca.models import Materia
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

class MateriaListView(LoginRequiredMixin, generic.ListView):
    model = Materia

class MateriaCreate(LoginRequiredMixin, CreateView):
    titulo = "Cadastrar Matéria"
    model = Materia
    fields = '__all__'
    success_url = reverse_lazy('materias')

class MateriaUpdate(LoginRequiredMixin, UpdateView):
    titulo = "Editar Matéria"
    model = Materia
    fields = '__all__'
    success_url = reverse_lazy('materias')

class MateriaDelete(LoginRequiredMixin, DeleteView):
    model = Materia
    success_url = reverse_lazy('materias')
