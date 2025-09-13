from django.db import models

class alunos(models.Model):
    nome = models.CharField(max_length=60),
    sobrenome = models.CharField(max_length=200),
    data_nascimento = models.DateField(),
    curso = models.CharField(max_length=200),
    matricula = models.IntegerField(),
    email = models.CharField(max_length=200),
    telefone = models.IntegerField(),
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

