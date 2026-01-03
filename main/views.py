from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from .forms import RespostaPesquisaForm
from .models import RespostaPesquisa

from .functions import get_infos_tabela

# Create your views here.

def home(request):
    return render(request, 'home.html')

def formulario(request):
    server_feedback = False
    if request.method == "POST":
        form = RespostaPesquisaForm(request.POST)
        if form.is_valid():
            obj = form.save()
            form = RespostaPesquisaForm()
            server_feedback = {
                "message" : 'Pesquisa salva com sucesso!',
                "style" : 'success'
            }
        else:
            print("ERROS:", form.errors)  # 👈 TESTE 4
            server_feedback = {
                "message" : 'Erro ao salvar pesquisa, por favor tente novamente',
                "style" : 'error'
            }
    else:
        form = RespostaPesquisaForm()

    return render(request, "formulario.html", {"form": form, "server_feedback": server_feedback})

def perfil(request):
    return render(request, "perfil.html")

def tabela(request):
    # Se não estiver logado, manda pro login
    if not request.user.is_authenticated:
        return redirect('/login')

    # Respostas em ordem alfabética (pelo nome)
    respostas = RespostaPesquisa.objects.all().order_by('nome_apelido')
    
    # Informações/Overall da tabela
    
    infos = get_infos_tabela()

    return render(request, 'tabela.html', {
        'respostas': respostas,
        'infos': infos
    })

def login(request):
    error = False

    if request.method == "POST":
        username = request.POST.get("user")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect("/perfil")  # ou qualquer página pós-login
        else:
            error = "Usuário ou senha inválidos, por favor tente novamente"

    return render(request, "login.html", {"error": error})

def logout_view(request):
    if request.method == "POST":
        logout(request)
    return redirect("/")