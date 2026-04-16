from django.urls import path
from . import views  # O '.' significa 'importe da pasta atual'

urlpatterns = [
    # Quando alguém visitar a URL raiz deste app (ex: /), 
    # chame a função 'app_view' que está em 'views.py'.
    # O 'name' é um apelido opcional que usaremos mais tarde.
    path('', views.home_view, name='home'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('status/', views.status_view, name='status'),
    path('cursos/', views.cursos_view, name='cursos'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('logout/', views.logout_view, name='logout'),

]