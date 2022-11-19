from django.shortcuts import render
from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioEmpleado import FormularioEmpleados
from web.models import Platos
from web.models import Empleados

# Create your views here.
# todas las vistas son funciones de python

def Home(request):
    return render(request,'home.html')

def todosplatos(request):
    platosConsultados=Platos.objects.all()
    data={
        'platos':platosConsultados
    }
    return render(request,'allplatos.html',data)

def PlatosVista(request):
    #rutina para la consulta de platos
    platosConsultados=Platos.objects.all()
    print(platosConsultados)
    # esta vista va a utilizar un formulario de django
    # entonces se debe crear un objetoo de la clase formularioPlatos()
    formulario=FormularioPlatos()
    # creamos un diccionario para enviar el formulario al html(template)
    data={
        'formulario':formulario,
        'bandera':False,
        'platos':platosConsultados
    }
    # recibimos los datos del form
    if request.method=="POST":
        datosFormulario=FormularioPlatos(request.POST)
        if datosFormulario.is_valid():
            datosLimpios=datosFormulario.cleaned_data
            print(datosLimpios)
            # construir un objeo/diccionario de envio de datos hacia la Base de datos
            platoNuevo=Platos(
                nombre=datosLimpios["nombre"],
                descripcion=datosLimpios["descripcion"],
                imagen=datosLimpios["foto"],
                precio=datosLimpios["precio"],
                tipo=datosLimpios["tipo"]
            )
            # intentar llevar los datos recogidos a la base de datos
            try:
                platoNuevo.save()
                data["bandera"]=True
                print("Exito guardando...")

            except Exception as error:
                print("Upsss",error)
                data["bandera"]=False

    return render(request,'menuplatos.html',data)

def EmpleadosVista(request):
    empleadosConsultados=Empleados.objects.all()
    formEmpleados=FormularioEmpleados()
    form2={
        'formEmpleados':formEmpleados,
        'bandera':False,
        'empleados':empleadosConsultados
    }
         #recibimos los datos del form
    if request.method=="POST":
        datosForm=FormularioEmpleados(request.POST)
        if datosForm.is_valid():
            datosEmp=datosForm.cleaned_data
            print(datosEmp)
            empleadoNuevo=Empleados(
                nombre = datosEmp["nombre"],
                apellidos = datosEmp["apellidos"],
                foto = datosEmp["foto"],
                cargo = datosEmp["cargo"],
                salario = datosEmp["salario"],
                contacto = datosEmp["contacto"]
            )
             #intentar llevar los datos recogidos a la base de datos
            try:
                empleadoNuevo.save()
                form2["bandera"]=True
                print("Exito guardando...")
            except Exception as error:
                print("Upsss",error)
                form2["bandera"]=False


    return render(request,'registrarempleados.html',form2)

def todosempleados(request):
    empleadosConsultados=Empleados.objects.all()
    form2={
        'empleados':empleadosConsultados
    }
    return render(request,'allempleados.html',form2)
