from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required   # Para proteger las vistas si no se a hecho login
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import  strip_tags
from django.core.mail import send_mail
from Cursos.models import Cursos, Asignaciones, LineaAsignacion
from Cursos.carro import Carro
from Usuarios.models import Estudiantes
from django.conf import settings


#-------------Catalogo de Cursos--------------------------

def cursos_all(request):
    cursos=Cursos.objects.all()
 
    return render(request, "cursos.html", {'cursos':cursos})

def curso_single(request, id):
    curso=Cursos.objects.get(codigo=id)
    
    return render(request, "curso-single.html", {'curso':curso})

#-----Curso-matriculado-----------------------
@login_required
def curso_matriculado(request, id):
    curso=Cursos.objects.get(codigo=id)
    
    return render(request, "curso_matriculado.html", {'curso':curso})

#-------------CARRITO---------------------------------------
@login_required(login_url="/inicio-sesion/")
def carrito(request):
    return render(request, "carrito.html")


def agregar_curso(request,curso_id):
    carro=Carro(request)
    curso=Cursos.objects.get(id=curso_id)
    carro.agregar(curso=curso) 
    return redirect('carrito')

def eliminar_curso(request,curso_id):
    carro=Carro(request)
    curso=Cursos.objects.get(id=curso_id)
    carro.eliminar(curso=curso)
    return redirect('carrito')  

def restar_curso(request, curso_id):
    carro = Carro(request)
    curso = Cursos.objects.get(id=curso_id)
    carro.restar(curso=curso)
    return redirect("cursos") 

def limpiar_carro(request, curso_id):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect('cursos')

#-------------PROCESADOR DE ASIGNACION---------------------------------------
def procesar_asignacion(request):
    asignacion=Asignaciones.objects.create(user=request.user)
    carro=Carro(request)
    lineas_asignaciones=[]
    for key, value in carro.carro.items():
        lineas_asignaciones.append(LineaAsignacion(

            curso_id=key,
            cupo=value["cupo"],
            user=request.user,
            asignacion=asignacion
        ))

    LineaAsignacion.objects.bulk_create(lineas_asignaciones)

    cursos_asignados = LineaAsignacion.objects.all()
    asignaciones = Asignaciones.objects.all()
    listado_todas_asignaciones = Cursos.objects.all()
    listado_estudiantes= Estudiantes.objects.all()

    # messages.success(request, "La asignacion se creado correctamente")

    # Lista de cursos asignados (sustituye con los nombres reales de los cursos)
    cursos_asignados = ["Curso 1", "Curso 2", "Curso 3"]

    subject = "¡Asignación de Cursos Satisfactoria - AcademiaUSAC!"
    message = f"""Estimado {request.user.first_name} {request.user.last_name},\n\n
            Te damos la bienvenida a AcademiaUSAC, tu plataforma educativa de confianza. Estamos encantados de tenerte como parte de nuestra comunidad y de anunciarte que has sido asignado a los siguientes cursos:\n\n
            {', '.join(cursos_asignados)}\n\n
            En AcademiaUSAC, encontrarás una amplia gama de recursos educativos para ayudarte a alcanzar tus metas académicas y profesionales. Estamos aquí para brindarte el apoyo que necesitas en tu viaje educativo. Si tienes alguna pregunta o necesitas asistencia, no dudes en contactarnos.\n\n
            Gracias por confiar en nosotros y por unirte a nuestra comunidad. Esperamos que tengas una experiencia educativa enriquecedora con nosotros.\n\n
            Atentamente,
            El equipo de AcademiaUSAC"""

    email_from = settings.EMAIL_HOST_USER
    recipient_list = [request.user.email]

    send_mail(subject, message, email_from, recipient_list)

    return redirect("asignaciones")

def enviar_mail(**kwargs):
    asunto="Asignacion de cursos satisfactoria - AcademiaUSAC"
    mensaje=render_to_string("asignacion.html", {
        "asignacion": kwargs.get("asignacion"),
        "lineas_asignaciones":kwargs.get("lineas_asignaciones"),
        "nombreusuario":kwargs.get("nombreusuario"),
    })

    mensaje_texto=strip_tags(mensaje)
    email_from = settings.EMAIL_HOST_USER
    to=kwargs.get("emailusuario")

    send_mail(asunto, mensaje_texto, email_from, [to], html_message=mensaje)