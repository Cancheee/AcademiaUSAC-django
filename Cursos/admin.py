from django.contrib import admin
from Cursos.models import Cursos, Asignaciones, LineaAsignacion



#--------------CURSOS------------------------------
class CursosAdmin(admin.ModelAdmin):
    list_display=('codigo', 'nombre', 'catedratico', 'horario', 'cupo_limite', 'precio', 'disponibilidad')
    search_fields=('codigo', 'nombre', 'catedratico', 'horario', 'cupo_limite', 'precio', 'disponibilidad')
    list_filter=('codigo', 'nombre', 'catedratico', 'horario', 'precio', 'disponibilidad')
    readonly_fields=('update','created')

admin.site.register(Cursos,CursosAdmin)


 #--------------ASIGNACIONES------------------------------

class AsignacionesAdmin(admin.ModelAdmin):
    list_display=('user', 'created_at')
    search_fields=['user', 'created_at']
    list_filter=['user', 'created_at']
    readonly_fields=['created_at']
admin.site.register(Asignaciones,AsignacionesAdmin)



class LineaAsignacionAdmin(admin.ModelAdmin):
    list_display=('user', 'curso', 'asignacion', 'cupo', 'created_at')
    search_fields=['user', 'curso', 'asignacion', 'cupo', 'created_at']
    list_filter=['user', 'curso', 'asignacion', 'cupo', 'created_at']
    readonly_fields=['created_at']
admin.site.register(LineaAsignacion,LineaAsignacionAdmin)