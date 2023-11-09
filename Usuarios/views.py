from django.views.generic import ListView, View
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from Usuarios.models import Estudiantes , Catedraticos
from Cursos.models import Cursos, Asignaciones, Notas
from Usuarios.forms import CustomUserCreationForm
import hashlib
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from axes.utils import reset    # type: ignore

def iniciar_sesion(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            usuario = authenticate(request=request, username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                reset(username=username)
                return redirect('perfil')
            else:
                messages.error(request,"Usuario no válido")
        else:
            messages.error(request,"Información no válida")

    form = AuthenticationForm()
    return render(request, "login.html", {"form":form})

#-------------Cerrar sesion----------------------
def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')


#-------------Estudiantes----------------------

def registro_exitoso(request):    
    
    return render(request, "registro-exitoso.html")


@login_required
def perfil(request):
    cursos_asignados = Notas.objects.all()
    asignaciones = Asignaciones.objects.all()
    listado_todas_asignaciones = Cursos.objects.all()
    listado_estudiantes= Estudiantes.objects.all()
    return render(request, "perfil.html", {"cursos_asignados":cursos_asignados, "listado_todas_asignaciones":listado_todas_asignaciones, 'listado_estudiantes': listado_estudiantes, 'asignaciones': asignaciones})

@login_required
def resumen_asignaciones(request):
    cursos_asignados = Notas.objects.all()
    asignaciones = Asignaciones.objects.all()
    listado_todas_asignaciones = Cursos.objects.all()
    listado_estudiantes= Estudiantes.objects.all()
    return render(request, "resumen_asignaciones.html", {"cursos_asignados":cursos_asignados, "listado_todas_asignaciones":listado_todas_asignaciones, 'listado_estudiantes': listado_estudiantes, 'asignaciones': asignaciones})

@login_required
def miscursos(request):
    cursos_asignados = Notas.objects.all()
    asignaciones = Asignaciones.objects.all()
    listado_todas_asignaciones = Cursos.objects.all()
    listado_estudiantes= Estudiantes.objects.all()
    return render(request, "cursos_asignados.html", {"cursos_asignados":cursos_asignados, "listado_todas_asignaciones":listado_todas_asignaciones, 'listado_estudiantes': listado_estudiantes, 'asignaciones': asignaciones})


class Registro(View):

    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, "registro.html", {"form": form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST, request.FILES)

        if form.is_valid():
            usuario = form.save()
            dpi = form.cleaned_data.get('dpi')
            img = form.cleaned_data.get("profile_image")
            telefono=form.cleaned_data.get("telefono")
            fecha_nacimiento=form.cleaned_data.get("fecha_nacimiento")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            usuario = authenticate(request=request, username=username, password=password)
            login(request, usuario)
            
            nuevo_usuario = Estudiantes(user=request.user, 
                                     username=request.user.username, 
                                     first_name=request.user.first_name, 
                                     last_name=request.user.last_name, 
                                     email=request.user.email, 
                                     DPI=dpi, 
                                     telefono=telefono,
                                     fecha_nacimiento=fecha_nacimiento,
                                     profile_image=img
                                     )
            nuevo_usuario.save()
            # Envio correo
            # subject="Registro en AcademiaUSAC"
            # message="Bienvenido a AcademiaUSAC ".format(request.user.first_name,request.user.last_name)
            # email_from=settings.EMAIL_HOST_USER
            # recipient_list=["{}".format(request.user.email)]
            # send_mail(subject, message, email_from, recipient_list)

            subject = "¡Bienvenido a AcademiaUSAC!"
            message = f"""Estimado {request.user.first_name} {request.user.last_name},\n \n
                        Te damos la bienvenida a AcademiaUSAC, tu plataforma educativa de confianza.
                        Estamos encantados de tenerte como parte de nuestra comunidad.\n\n 
                        En AcademiaUSAC, encontrarás una amplia gama de cursos y recursos educativos
                        para ayudarte a alcanzar tus metas académicas y profesionales.\n\n
                        Si tienes alguna pregunta o necesitas asistencia, no dudes en contactarnos. 
                        Estamos aquí para ayudarte en tu viaje educativo.\n\n 
                        Gracias por unirte a nosotros y esperamos que tengas una experiencia educativa 
                        enriquecedora con nosotros.\n\n
                        Atentamente,\n 
                        El equipo de AcademiaUSAC"""

            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.user.email]

            send_mail(subject, message, email_from, recipient_list)


            return redirect('registro_exitoso')
        else:
            for field_name, error_messages in form.errors.items():
                for msg in error_messages:
                    messages.error(request, f"{field_name}: {msg}")

            return render(request, "registro.html", {"form": form})
        

