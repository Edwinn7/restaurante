from django.shortcuts import render

# Create your views here.
# todas las vistas son funciones de python

def Home(request):
    return render(request,'home.html')
