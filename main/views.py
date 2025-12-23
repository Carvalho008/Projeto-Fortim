from django.shortcuts import render, redirect
from .forms import RespostaPesquisaForm
from .models import RespostaPesquisa

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
