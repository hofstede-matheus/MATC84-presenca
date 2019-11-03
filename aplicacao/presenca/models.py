from django.db import models

# Create your models here.

from django.urls import reverse # Used to generate URLs by reversing the URL patterns

from django.contrib.auth.models import User

class Professor(models.Model):
    # Campos
    usuario = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)

    # Metadados

    # Metodos


class Aluno(models.Model):
    # Campos
    usuario = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)

    OPCOES_CURSO = (
        ('c', 'Ciência da Computação'),
        ('s', 'Sistemas de Informação'),
        ('l', 'Licenciatura em Computação'),
        ('e', 'Engenharia da Computação'),
    )

    curso = models.CharField(
        max_length=1,
        choices=OPCOES_CURSO,
        help_text='Selecione seu curso',
    )

    # Metadados

    # Metodos


class Materia(models.Model):
    # Campos
    codigo = models.CharField(max_length=10, help_text="Coloque o código da matéria, como consta no SIAC")
    nome = models.CharField(max_length=100, help_text="Coloque o nome da matéria, como consta no SIAC")

    # Metadados

    # Metodos
    def __str__(self):
        return f'{self.codigo} - {self.nome}'


class Turma(models.Model):
    # Campos
    professor = models.ForeignKey(Professor, on_delete = models.SET_NULL, null = True)
    materia = models.ForeignKey(Materia, on_delete = models.SET_NULL, null = True)
    codigo = models.PositiveIntegerField()
    total_aulas = models.PositiveIntegerField()
    
    alunos = models.ManyToManyField(Aluno)

    # Metadados

    # Metodos

class Presenca(models.Model):
    # Campos
    dia_horario = models.DateTimeField(auto_now_add=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.SET_NULL, null=True)
    materia = models.ForeignKey(Materia, on_delete = models.SET_NULL, null = True) 
    presente = models.BooleanField(default=False)

    # Metadados

    # Metodos
