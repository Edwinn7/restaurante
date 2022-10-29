from django.shortcuts import render
from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioEmpleado import FormularioEmpleados

# Create your views here.
# todas las vistas son funciones de python

def Home(request):
    return render(request,'home.html')

def Platos(request):
    # esta vista va a utilizar un formulario de django
    # entonces se debe crear un objetoo de la clase formularioPlatos()
    formulario=FormularioPlatos()
    # creamos un diccionario para enviar el formulario al html(template)
    data={
        'formulario':formulario
    }
    return render(request,'menuplatos.html',data)

def Empleados(request):
    formEmpleados=FormularioEmpleados()
    form2={
        'formEmpleados':formEmpleados
    }
    return render(request,'registrarempleados.html',form2)