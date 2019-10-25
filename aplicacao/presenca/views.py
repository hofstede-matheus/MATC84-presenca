from django.shortcuts import render

# Create your views here.

from presenca.models import Pessoa, Professor, Aluno, Materia, Turma, Presenca

def home(request):

    context = {

    }

    # Render the HTML template home.html with the data in the context variable
    return render(request, 'home.html', context=context)
