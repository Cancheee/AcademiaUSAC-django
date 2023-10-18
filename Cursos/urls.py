
from django.contrib import admin
from django.urls import path, include
from Cursos import views



urlpatterns = [

    path('', views.cursos_all, name="cursos"),
    #path('curso-single/', views.curso_single, name="curso_single"),
    path('curso-single/<int:id>', views.curso_single, name="curso_single"),

    #Carrito
    path('carro/agregar/<int:id>', views.agregar_curso, name="agregar"),
    path('carro/restar/<int:id>', views.restar_curso, name="restar"),
    path('carro/eliminar/<int:id>', views.eliminar_curso, name="eliminar"),
    path('carro/limpiar/<int:id>', views.limpiar_carro, name="limpiar"),
]


