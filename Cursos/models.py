from django.db import models
from django.core.exceptions import ValidationError
from Usuarios.models import Catedraticos

class Cursos(models.Model):
    nombre_curso = models.CharField(max_length=70, null=False, verbose_name='Nombre del Curso')         # Nombre del Curso
    catedratico = models.ForeignKey(Catedraticos, on_delete=models.CASCADE, verbose_name='Catedratico')
    #catedratico = models.CharField(max_length=30, null=False, verbose_name='Catedratico')              # Catedratico
    codigo = models.IntegerField(null=False, unique=True, verbose_name='Codigo')                        # Codigo
    horario=models.CharField(max_length=16, null=False, verbose_name='Horario')                         # Horario
    costo = models.FloatField(null=False, verbose_name='Costo')                                         # Costo
    descripcion = models.CharField(max_length=300)                                                      # Descripcion del curso
    imagen = models.ImageField(upload_to='Cursos/')                                                     # Imagen del Curso
    cupo= models.IntegerField(null=False, default= 0)                                                   # Cupo
    disponibilidad = models.BooleanField(verbose_name='Disponibilidad')                                 # Disponibilidad de Cupo
    created = models.DateTimeField(auto_now_add=True)                                                   # Creacion
    update = models.DateTimeField(auto_now=True)                                                        # Modificacion

    def clean(self):
        # Verificar si el catedrático ya tiene cursos con el mismo horario
        cursos_con_mismo_horario = Cursos.objects.filter(catedratico=self.catedratico, horario=self.horario).exclude(pk=self.pk)
        if cursos_con_mismo_horario.exists():
            raise ValidationError("El catedrático ya tiene un curso con el mismo horario.")
    class Meta:
        db_table = 'Cursos'
        verbose_name='Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        #return self.nombre_curso
        return '%s %s / %s / %s / Q%s' %(self.codigo, self.nombre_curso, self.catedratico, self.horario, self.costo)
 