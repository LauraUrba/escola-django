from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')

def cadastro_alunos(request):
    return render(request, 'alunos.html')

def salvar_aluno(request):
    if request.method == 'POST':

        nome_aluno = request.POST['nome_aluno']
        sobrenome = request.POST['sobrenome_aluno']
        curso = request.POST['curso_aluno']
        email = request.POST['email_aluno']
        endereco = request.POST['endereco_aluno']

        return render(request, 'alunos.html', context ={
            'nome_aluno': nome_aluno,
            

        })
    return HttpResponse('Método não permitido', status=405)



        titulo_livro = request.POST['titulo_livro']
        autor_livro = request.POST['autor_livro']
        editora = request.POST['editora']
        return render(request, 'livros.html', context={
            'titulo_livro': titulo_livro,
            'autor_livro': autor_livro,
            'editora': editora
        })
    return HttpResponse('Método não permitido', status=405)