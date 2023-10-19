from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.conf import settings
# from Cursos.models import Cursos
User = get_user_model()

# Create your models here.

class Estudiantes(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=150, null=False, default='nombre')
    last_name = models.CharField(max_length=150, null=False, default='Apellidos')
    username = models.CharField(max_length=150, null=False, default=user)
    email = models.EmailField(max_length=150, default="direccion@gmail.com")
    DPI = models.CharField(max_length=13, null=False, default="0")
    telefono=models.CharField(max_length=8, null=False, default="0")
    fecha_nacimiento=models.DateField()
    profile_image = models.ImageField(upload_to='Estudiantes/')

    login_attempts = models.IntegerField(null=False, default=0)
    active_account = models.BooleanField(null=False, default=True)

    def str(self):
        return self.username

    class Meta:
        db_table = 'Estudiantes'
        verbose_name='Estudiante'
        verbose_name_plural = 'Estudiantes'
        ordering=['id']

class Catedraticos(models.Model):
    nombre = models.CharField(max_length=30, null=False)                    # Nombre
    apellido = models.CharField(max_length=30, null=False)                  # Apellido
    ## DPI SOLO 13 NUMEROS
    dpi_regex = r'^[0-9]{13}$'
    DPI = models.CharField(
        max_length=13,
        unique=True,
        validators=[
            RegexValidator(
                regex=dpi_regex,
                message="El DPI debe contener exactamente 13 dígitos numéricos.",
            )
        ]
    )                     # DPI
    password = models.CharField(max_length=15, null=False)                # Contraseña

    class Meta:
        db_table = 'Catedraticos'
        verbose_name='Catedratico'
        verbose_name_plural = 'Catedraticos'
    
    def __str__(self):
        #return self.nombre_curso
        return '%s %s' %(self.nombre, self.apellido)