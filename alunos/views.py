from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Aluno

# Create your views here.
def home(request):
    return render(request, 'index.html')

def pagina_alunos(request):
    return render(request, 'alunos.html')

'''
def salvar_aluno(request):
    if request.method == 'POST':
        nome_aluno = request.POST['nome_aluno']
        sobrenome = request.POST['sobrenome_aluno']
        curso = request.POST['curso_aluno']
        email = request.POST['email_aluno']
        endereco = request.POST['endereco_aluno']

        return render(request, 'alunos.html', context ={
            'nome_aluno': nome_aluno,
            'sobrenome_aluno': sobrenome,
            'curso_aluno': curso,
            'email_aluno': email,
            'endereco_aluno': endereco})
    
    return HttpResponse('Método não permitido', status=405)
'''

def cadastro_alunos(request):
   if request.method == 'POST':
       matricula_id = request.POST.get('matricula_id')
       nome_aluno = request.POST['nome_aluno']
       sobrenome = request.POST['sobrenome_aluno']
       curso = request.POST['curso_aluno']
       email = request.POST['email_aluno']
       endereco = request.POST['endereco_aluno']
       matricula = request.POST['matricula_aluno']
       telefone = request.POST['telefone_aluno']
       data_nascimento = request.POST['data_nascimento_aluno']

       if matricula_id:
        aluno = Aluno.objects.get(id=matricula_id)
        aluno.nome = nome_aluno
        aluno.sobrenome = sobrenome
        aluno.curso = curso
        aluno.email = email
        aluno.endereco = endereco
        aluno.matricula = matricula
        aluno.telefone = telefone
        aluno.data_nascimento = data_nascimento
        aluno.save()


       else:
           Aluno.objects.create(
               nome = nome_aluno,
               sobrenome = sobrenome,
               curso = curso,
               email = email,
               endereco = endereco,
               matricula = matricula,
               telefone = telefone,
               data_nascimento = data_nascimento
           )
           return redirect('cadastro_alunos')

   aluno = Aluno.objects.all()
   return render(request, 'alunos.html', {'alunos': aluno})
