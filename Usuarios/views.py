from django.views.generic import ListView, View
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from Usuarios.models import Estudiantes, Catedraticos
from Usuarios.forms import  EstudiantesForm
from Usuarios.forms import EstudianteRegistroForm, UserRegisterForm
import hashlib
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.core.mail import send_mail, EmailMessage
from django.conf import settings

#-------------Inicio de Sesion General----------------------
def iniciar_sesion(request):
    if request.method=="POST":
        usuario = request.POST.get('username')
        form=AuthenticationForm(request, data=request.POST)

        # Estudiantes
        if Estudiantes.objects.filter(usuario=usuario).exists():
            estudiante = Estudiantes.objects.get(usuario=usuario)

            if form.is_valid():
                nombre_usuario=form.cleaned_data.get('username')
                contraseña=form.cleaned_data.get('password')
                estudiante.intentos_fallidos = 0    
                estudiante.save()
                usuario=authenticate(username=nombre_usuario, password=contraseña)
                if usuario is not None:
                    login(request, usuario)
                    return redirect('inicio')
                else:
                    messages.error(request, "Credenciales Incorrectas")

            else:
                nombre_usuario=form.cleaned_data.get('username')
                contraseña=form.cleaned_data.get('password')
<<<<<<< HEAD
                # contraseña = hashlib.sha256(contraseña.encode()).hexdigest() # Encriptacion
=======
                contraseña = hashlib.sha256(contraseña.encode()).hexdigest() # Encriptacion
>>>>>>> 836a75084883c5b0ed27b181f4f540aba4c03301
                intentos_totales=3
                estudiante.intentos_fallidos += 1
                estudiante.save()
                intentos_restantes=intentos_totales-estudiante.intentos_fallidos
                intentos_fallidos = estudiante.intentos_fallidos

                if intentos_restantes > 1:
                    mensaje = f'Te quedan {intentos_restantes} intentos, si no tu cuenta será bloqueada'
                elif intentos_restantes == 0:
                    mensaje = f'Tu cuenta a sido bloqueada por 3 intentos de contraseña incorrecta'
                else: 
                    mensaje = f'Te quedan {intentos_restantes} intento, si no tu cuenta será bloqueada'

<<<<<<< HEAD
                if estudiante.activo == False:
                    mensaje= 'Tu cuenta se encuentra bloqueada'
                    messages.error(request, mensaje)
                elif intentos_fallidos == 3:
                    estudiante.activo = False
                    estudiante.save()
                    messages.error(request, mensaje)
                
=======

                if intentos_fallidos == 3:
                    estudiante.activo = False
                    estudiante.save()
                    messages.error(request, mensaje)
                if estudiante.activo == False:
                    mensaje= 'Tu cuenta se encuentra bloqueada  '
                    messages.error(request, mensaje)
>>>>>>> 836a75084883c5b0ed27b181f4f540aba4c03301
                else:
                    messages.error(request, mensaje)
                
                

        # Catedraitocos o Admin
        else:
            if form.is_valid():
                nombre_usuario=form.cleaned_data.get('username')
                contraseña=form.cleaned_data.get('password')
                usuario=authenticate(username=nombre_usuario, password=contraseña)
                if usuario is not None:
                    login(request, usuario)
                    return redirect('inicio')
                else:
                    messages.error(request, "Credenciales Incorrectas")
            else:
                messages.error(request, "Informacion incorrecta")
    
    form=AuthenticationForm()
    return render(request, 'login.html', {'form':form})

#-------------Cerrar sesion----------------------
def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')


#-------------Estudiantes----------------------

def registro_exitoso(request):    
    
    return render(request, "registro-exitoso.html")


def registro(request):
    if request.method == 'POST':
        # Obtén los valores ingresados en el formulario
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        dpi = request.POST.get('dpi')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        telefono = request.POST.get('telefono')
        usuario = request.POST.get('usuario')
        correo = request.POST.get('correo')
        contraseña = request.POST.get('contraseña')
        confirm_password = request.POST.get('confirm_password')
        imagen= request.POST.get('imagen')

        # Verifica si el usuario ya existe en la base de datos
        if Estudiantes.objects.filter(usuario=usuario).exists():
            return render(request, "registro.html", {"error": "El usuario ya está registrado.", "form": EstudiantesForm(request.POST)})

        # Verifica si el correo ya existe en la base de datos
        if Estudiantes.objects.filter(correo=correo).exists():
            return render(request, "registro.html", {"error": "El correo ya está registrado.", "form": EstudiantesForm(request.POST)})

        # Verifica que las contraseñas coincidan
        if contraseña != confirm_password:
            error = "Las contraseñas no coinciden"
            return render(request, 'registro.html', {'error': error})
        
        # Verifica las condiciones de la contraseña
        if (len(contraseña) < 8):
            return render(request, "registro.html", {"error": "La contraseña debe tener minimo 8 caracteres.", "form": EstudiantesForm(request.POST)},)
        if (not any(c.isupper() for c in contraseña)):
            return render(request, "registro.html", {"error": "La contraseña debe tener al menos 1 letra mayuscula.", "form": EstudiantesForm(request.POST)},)
        if (not any(c.isdigit() for c in contraseña)):
            return render(request, "registro.html", {"error": "La contraseña debe tener al menos 1 digito", "form": EstudiantesForm(request.POST)},)
        if (not any(c in "!@#$%^&*()_+[]{};:'\"\\|,.<>/?-" for c in contraseña)):
             return render(request, "registro.html", {"error": "La contraseña debe tener al menos 1 simbolo", "form": EstudiantesForm(request.POST)},)
        
        # Verifica si el dpi ya existe
        if Estudiantes.objects.filter(dpi=dpi).exists():
            return render(request, "registro.html", {"error": "El DPI ya está registrado.", "form": EstudiantesForm(request.POST)})

<<<<<<< HEAD
        # Envio correo
        subject="Registro en AcademiaUSAC"
        message="Bienvenido a AcademiaUSAC ".format(nombre,apellido)
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["{}".format(correo)]
        send_mail(subject, message, email_from, recipient_list)
        
=======
>>>>>>> 836a75084883c5b0ed27b181f4f540aba4c03301
        # Encriptacion
        # contraseña = hashlib.sha256(contraseña.encode()).hexdigest()
        # Crea una instancia del modelo con los valores del formulario
        nuevo_usuario = Estudiantes(
            nombre=nombre,
            apellido=apellido,
            dpi=dpi,
            fecha_nacimiento=fecha_nacimiento,
            telefono=telefono,
            usuario=usuario,
            correo=correo,
            contraseña=contraseña,
            imagen=imagen,
        )
        # Guarda el nuevo usuario en la base de datos
        nuevo_usuario.save()
        # Redirige a una página de éxito o a donde desees después del registro
        return render(request, 'registro-exitoso.html')
    # Si la solicitud no es un POST, simplemente renderiza el formulario vacío
    return render(request, 'registro.html')


# class Registro(View):
    
#     def get(self, request):
#         form=UserRegisterForm()
#         return render(request, 'registro.html', {'form':form})
        

#     def post(self, request):
#         form=UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             ## Esto seria en caso de que queremos que al registrarse se inicie automaticamente
#             # usuario=form.save()
#             # login(request, usuario)
#             username=form.cleaned_data.get('username')
#             password=form.cleaned_data.get('password1')
#             nuevo_usuario = Estudiantes(
#                 user=request.user,
#                 username=request.user.username,
#                 fisrt_name=request.user.first_name,
#                 last_name=request.user.last_name, 
#                 email=request.user.email, 
#                 dpi=dpi, 
                
#                 )
#             nuevo_usuario.save()

#             return redirect('registro_exitoso')
        
#         else:
#             for msg in form.error_messages:
#                 messages.error(request, form.error_messages[msg])
            
#             return render(request, 'registro.html', {'form':form})






# def registro(request):
#     if request.method == 'POST':
#         form = EstudianteRegistroForm(request.POST)
#         if form.is_valid():
#             estudiante = form.save()
#             login(request, estudiante)  # Iniciar sesión automáticamente después del registro
#             return redirect('registro_exitoso')  # Redirigir a la página de inicio o dashboard

#     else:
#         form = EstudianteRegistroForm()
#     return render(request, 'registro.html', {'form': form})

# def sesion(request):
    
    # return render(request, "sesion.html")