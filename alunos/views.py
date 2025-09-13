from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def cadastro_alunos(request):
    return render(request, 'alunos.html')