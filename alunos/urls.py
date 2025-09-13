from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.home),
    path('alunos/', views.cadastro_alunos, name='alunos'),
]