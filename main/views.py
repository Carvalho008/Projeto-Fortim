from django.shortcuts import render, redirect
from .forms import RespostaPesquisaForm
from .models import RespostaPesquisa

# Create your views here.

def home(request):
    return render(request, 'home.html')

def formulario(request):
    if request.method == "POST":
        print("CHEGOU POST")  # 👈 TESTE 1
        form = RespostaPesquisaForm(request.POST)
        if form.is_valid():
            print("FORM VALID")  # 👈 TESTE 2
            obj = form.save()
            print("SALVO:", obj.id)  # 👈 TESTE 3
            return redirect("formulario")
        else:
            print("ERROS:", form.errors)  # 👈 TESTE 4
    else:
        form = RespostaPesquisaForm()

    return render(request, "formulario.html", {"form": form})
