from django.db import models

# Create your models here.

from django.urls import reverse # Used to generate URLs by reversing the URL patterns

import uuid # Required for unique book instances

class Pessoa(models.Model):
    # Campos
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    nome = models.CharField(max_length=45)
    sobrenome = models.CharField(max_length=45)
    email = models.EmailField()

    # Metadados

    # Metodos
    def __str__(self):
      return f'{self.nome} {self.sobrenome}'


class Professor(models.Model):
    # Campos
    pessoa = models.OneToOneField(Pessoa, on_delete = models.CASCADE, primary_key = True)

    # Metadados

    # Metodos


class Aluno(models.Model):
    # Campos
    pessoa = models.OneToOneField(Pessoa, on_delete = models.CASCADE, primary_key = True)

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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    codigo = models.CharField(max_length=10, help_text="Coloque o código da matéria, como consta no SIAC")
    nome = models.CharField(max_length=100, help_text="Coloque o nome da matéria, como consta no SIAC")

    # Metadados

    # Metodos


class Turma(models.Model):
    # Campos
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    professor = models.ForeignKey(Professor, on_delete = models.SET_NULL, null = True)
    materia = models.ForeignKey(Materia, on_delete = models.SET_NULL, null = True)
    codigo = models.PositiveIntegerField()
    total_aulas = models.PositiveIntegerField()
    
    alunos = models.ManyToManyField(Aluno)

    # Metadados

    # Metodos

class Presenca(models.Model):
    # Campos
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    dia_horario = models.DateTimeField(auto_now_add=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.SET_NULL, null=True)
    materia = models.ForeignKey(Materia, on_delete = models.SET_NULL, null = True) 
    presente = models.BooleanField(default=False)

    # Metadados

    # Metodos
