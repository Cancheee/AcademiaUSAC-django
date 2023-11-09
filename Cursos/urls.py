
from django.contrib import admin
from django.urls import path, include
from Cursos import views



urlpatterns = [

    path('', views.cursos_all, name="cursos"),
    #path('curso-single/', views.curso_single, name="curso_single"),
    path('curso-single/<int:id>', views.curso_single, name="curso_single"),
    path('curso/<int:id>', views.curso_matriculado, name="entrar"),
    path('curso/notas/<int:id>', views.notas, name="notas"),
    path('curso/certificacion/<int:id>', views.generar_pdf, name='certificacion'),
    #Carrito
    path('carrito', views.carrito, name="carrito"),
    path('carrito/agregar/<int:curso_id>', views.agregar_curso, name="agregar"),
    path("carrito/restar/<int:curso_id>/", views.restar_curso, name="restar"),
    path('carrito/eliminar/<int:curso_id>', views.eliminar_curso, name="eliminar"),
    path('carrito/limpiar/<int:curso_id>', views.limpiar_carro, name="limpiar"),
    #Procesar asignacion
    path('asignacion', views.procesar_asignacion, name="procesar_asignacion"),
]


