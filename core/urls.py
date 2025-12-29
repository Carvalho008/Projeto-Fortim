from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('formulario/', views.formulario, name='formulario'),
    path('perfil/', views.perfil, name='perfil'),
    path('tabela/', views.tabela, name='tabela'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
