from email import message
from django.shortcuts import render, redirect
from productos.models import Productos


def index(request):
    return render(request,"index.html")

def Donacion(request):
    return render(request,"Donacion.html")

def Contacto(request):
    return render(request,"Contacto.html")    

def login(request):
    return render(request,"login.html")

def Compras(request):
    productos = Productos.objects.all()
    contexto = {'listadoProductos':productos}
    return render(request,"Compras.html",contexto)

def Seguimiento(request):
    nombre_Seguimiento ="Seguimiento"
    contexto = {'Seguimiento':nombre_Seguimiento}
    return render(request,"Seguimiento.html",contexto)   


def eliminarProducto(request,id):
    borraproducto = Productos.objects.get(id=id)
    borraproducto.delete()
    return redirect('/Compras/')


def agregarPelicula(request):

    Productos.objects.create(
                            nombre="objeto",
                            descripcion ="descripcion",
                            disponible = 1,
                            cantidad = 5)
    return redirect('/Compras/')       


def reguistro(request):
     return render(request,"login.html") 