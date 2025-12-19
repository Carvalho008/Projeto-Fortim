from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def formulario(request):
    return render(request, 'formulario.html')