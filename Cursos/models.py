from django.db import models
from django.core.exceptions import ValidationError
from Usuarios.models import Catedraticos
from django.db.models import F, Sum, FloatField
from django.contrib.auth import get_user_model
User = get_user_model()

#--------------CURSOS------------------------------
class Cursos(models.Model):
    nombre = models.CharField(max_length=70, null=False, verbose_name='Nombre del Curso')               # Nombre del Curso
    codigo = models.IntegerField(null=False, unique=True, verbose_name='Codigo')  
    catedratico = models.ForeignKey(Catedraticos, on_delete=models.CASCADE, verbose_name='Catedratico')
    horario=models.CharField(max_length=16, null=False, verbose_name='Horario')                         # Horario
    precio = models.FloatField(null=False, verbose_name='Precio')                                       # Precio
    descripcion = models.CharField(max_length=300)                                                      # Descripcion del curso
    imagen = models.ImageField(upload_to='Cursos/')                                                     # Imagen del Curso
    cupo_limite = models.PositiveIntegerField()
    cupo_actual = models.PositiveIntegerField(default=0)                                                # Inicialmente, el cupo actual es 0                                                                                                   # Cupo
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
        return '%s / %s / %s / %s / Q%s' %(self.codigo, self.nombre   , self.catedratico, self.horario, self.precio)
 
 #--------------ASIGNACIONES------------------------------
class Asignaciones(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def total(self):
        return self.LineaAsignacion_set.aggregate(
                total=Sum(F("precio"),output_field=FloatField())
        ) ['total']
    
    class Meta:
        db_table = 'Asignaciones'
        verbose_name='Asignacion'
        verbose_name_plural = 'Asignaciones'
        ordering=['id']

class Notas(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    curso=models.ForeignKey(Cursos, on_delete=models.CASCADE)
    asignacion=models.ForeignKey(Asignaciones, on_delete=models.CASCADE)
    cupo=models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    nota1 = models.DecimalField(max_digits=5, decimal_places=2, null=True, verbose_name='Nota 1')
    nota2 = models.DecimalField(max_digits=5, decimal_places=2, null=True, verbose_name='Nota 2')
    nota3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, verbose_name='Nota 3')
    nota_final = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Nota Final')

    def save(self, *args, **kwargs):
        self.nota_final = (self.nota1 + self.nota2 + self.nota3) / 3
        super(Notas, self).save(*args, **kwargs)


    def __str__(self):
        return f"{self.cupo}"
    
    @property
    def total(self):
        pass
    class Meta:
        db_table = 'Notas'
        verbose_name='Notas'
        verbose_name_plural = 'Notas'
        ordering=['id']
#-------NOTAS-----------------



