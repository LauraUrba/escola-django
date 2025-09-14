from django.urls import path, include
from alunos import views

urlpatterns = [
    
    path('', views.home),
    path('index/', views.home, name='home'),
    path('alunos/', views.cadastro_alunos, name='alunos'),
    path('', views.cadastro_alunos, name='cadastro_alunos'),
]