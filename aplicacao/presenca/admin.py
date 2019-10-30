from django.contrib import admin

# Register your models here.

from presenca.models import Professor, Aluno, Materia, Turma, Presenca 

admin.site.register(Professor)
admin.site.register(Aluno)
admin.site.register(Materia)
admin.site.register(Turma)
admin.site.register(Presenca)
