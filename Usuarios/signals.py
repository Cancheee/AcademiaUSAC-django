from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from Cursos.models import Catedraticos  # Importamos el modelo Catedraticos
from .models import Estudiantes
#Este codigo nos servira para darles un incio de sesion a catedraticos desde el models

@receiver(post_save, sender=Catedraticos)
def create_user(sender, instance, created, **kwargs):
    if created:
        username = instance.nombre + instance.apellido
        user = User(username=username)
        user.set_password(instance.password)  
        user.is_staff = True  # Hacer que todos los catedráticos sean staff por defecto
        user.save()

        # Añadir al grupo 'catedraticos' , antes de añadir catedraticos tendremos que añadirlo
        Catedraticos_group, created = Group.objects.get_or_create(name='Catedraticos')
        user.groups.add(Catedraticos_group)


@receiver(post_save, sender=Catedraticos)
def update_user(sender, instance, **kwargs):
    try:
        user = User.objects.get(username=instance.nombre + instance.apellido)
        user.set_password(instance.password)
        user.save()
    except User.DoesNotExist:
        pass

@receiver(post_delete, sender=Catedraticos)
def delete_user(sender, instance, **kwargs):
    try:
        username = instance.nombre + instance.apellido
        user = User.objects.get(username=username)
        user.delete()
    except User.DoesNotExist:
        pass




@receiver(post_save, sender=Estudiantes)
def create_user_estudents(sender, instance, created, **kwargs):
    if created:
        user = User(username=instance.usuario)
        user.set_password(instance.contraseña)
        user.save()

        # Añadir al grupo 'catedraticos' , antes de añadir catedraticos tendremos que añadirlo
        Estudiantes_group, created = Group.objects.get_or_create(name='Estudiantes')
        user.groups.add(Estudiantes_group)


@receiver(post_save, sender=Estudiantes)
def update_user_estudents(sender, instance, **kwargs):
    try:
        user = User.objects.get(username=instance.usuario)
        user.set_password(instance.contraseña)
        user.save()

        # Verificar si el campo 'activo' ha cambiado a False
        if not instance.activo and user.is_active:
            user.is_active = False
            user.save()

        if instance.activo and not user.is_active:
            user.is_active = True
            user.save()

    except User.DoesNotExist:
        pass

@receiver(post_delete, sender=Estudiantes)
def delete_user_estudents(sender, instance, **kwargs):
    try:
        user = User.objects.get(username=instance.usuario)
        user.delete()
    except User.DoesNotExist:
        pass