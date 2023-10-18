from django.contrib import admin

# Register your models here.
from Cursos.models import Cursos

class CursosAdmin(admin.ModelAdmin):
    list_display=('codigo', 'nombre_curso', 'catedratico', 'horario', 'cupo', 'costo', 'disponibilidad')
    search_fields=('codigo', 'nombre_curso', 'catedratico', 'horario', 'cupo', 'costo', 'disponibilidad')
    list_filter=('codigo', 'nombre_curso', 'catedratico', 'horario', 'costo', 'disponibilidad')
    readonly_fields=('update','created')

admin.site.register(Cursos,CursosAdmin)