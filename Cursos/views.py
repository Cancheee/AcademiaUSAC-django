from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required   # Para proteger las vistas si no se a hecho login
from Cursos.models import Cursos

from Cursos.carro import Carro

#-------------Catalogo de Cursos--------------------------
@login_required
def cursos_all(request):
    cursos=Cursos.objects.all()
 
    return render(request, "cursos.html", {'cursos':cursos})

def curso_single(request, id):
    curso=Cursos.objects.get(codigo=id)
    
    return render(request, "curso-single.html", {'curso':curso})



#-------------CARRITO---------------------------------------
def agregar_curso(request,curso_id):
    carro=Carro(request)
    producto=Cursos.objects.get(id=curso_id)
    carro.agregar(producto=producto)
    return redirect('cursos')

def eliminar_curso(request,producto_id):
    carro=Carro(request)
    producto=Cursos.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect('cursos')   

def restar_curso(request,producto_id):
    carro=Carro(request)
    producto=Cursos.objects.get(id=producto_id)
    carro.restar_cupo(producto=producto)
    return redirect('cursos')

def limpiar_carro(request, curso_id):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect('cursos')