from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.conf import settings
User = get_user_model()

# class EstudianteManager(BaseUserManager):
#     def create_user(self, username, email, password=None, **extra_fields):
#         if not username:
#             raise ValueError("El campo 'username' es obligatorio")
#         if not email:
#             raise ValueError("El campo 'email' es obligatorio")
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError("Superuser debe tener is_staff=True.")
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError("Superuser debe tener is_superuser=True.")

#         return self.create_user(username, email, password, **extra_fields)

# class Estudiantes(AbstractBaseUser, PermissionsMixin):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     usuario = models.CharField(max_length=15, unique=True)
#     correo = models.EmailField(unique=True)
#     nombre = models.CharField(max_length=15)
#     apellido = models.CharField(max_length=15)
#     dpi = models.CharField(max_length=13)
#     fecha_nacimiento = models.DateField()
#     telefono = models.CharField(max_length=8)
#     imagen = models.ImageField(upload_to='estudiantes/', blank=True, null=True)

#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = EstudianteManager()

#     # Define related_name para evitar conflictos con los campos de grupos y permisos
#     groups = models.ManyToManyField('auth.Group', related_name='estudiantes')
#     user_permissions = models.ManyToManyField('auth.Permission', related_name='estudiantes')


#     USERNAME_FIELD = 'usuario'
#     REQUIRED_FIELDS = ['correo']

#     class Meta:
#         db_table = 'Estudiantes'
#         verbose_name='Estudiante'
#         verbose_name_plural = 'Estudiantes'

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=30, null=False)                    # Nombre
    apellido = models.CharField(max_length=30, null=False)                  # Apellido
    dpi = models.CharField(max_length=13,unique=True,validators=[
            RegexValidator(regex=r'^[0-9]{13}$',message="El DPI debe contener exactamente 13 dígitos numéricos.",)])                                                                                       # DPI
    fecha_nacimiento = models.DateField(verbose_name='Fecha de Nacimiento')                        # Fecha de Nacimiento
    telefono = models.IntegerField()                                                        # Telefono
    usuario = models.CharField(max_length=10, null=False, unique=True)                      # Usuario
    correo = models.EmailField(unique=True)                                                 # Correo
    contraseña = models.CharField( null=False)                                # Contraseña
    imagen = models.ImageField(upload_to='Estudiantes/', blank=False, null=False)        # Imagen
    # Otros campos personalizados relacionados con el perfil del estudiante
    intentos_fallidos = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)
    class Meta:
        db_table = 'Estudiantes'
        verbose_name='Estudiante'
        verbose_name_plural = 'Estudiantes'

    def __str__(self):
        #return self.nombre_curso
        return ' %s / %s %s / %s' %(self.usuario, self.nombre, self.apellido, self.correo)


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