from django.contrib import admin
from Cursos.models import Cursos, Asignaciones, Notas
from import_export.admin import ImportExportModelAdmin


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
    readonly_fields=['created_at', 'user']
admin.site.register(Asignaciones,AsignacionesAdmin)

class MemberAdmin(ImportExportModelAdmin):
    list_display=('user', 'curso', 'asignacion', 'created_at', 'nota_final')
    search_fields=['user', 'curso', 'asignacion']
    list_filter=['user', 'curso', 'asignacion']
    readonly_fields=['user', 'curso','asignacion', 'nota_final']
    exclude = ['cupo']  # Campos que quieres ocultar
    fields = ['user', 'curso', 'asignacion', 'nota1', 'nota2', 'nota3', 'nota_final']
    pass

class NotasAdmin(admin.ModelAdmin):
    list_display=('user', 'curso', 'asignacion', 'created_at', 'nota_final')
    search_fields=['user', 'curso', 'asignacion']
    list_filter=['user', 'curso', 'asignacion']
    readonly_fields=['user', 'curso','asignacion', 'nota_final']
    exclude = ['cupo']  # Campos que quieres ocultar
    fields = ['user', 'curso', 'asignacion', 'nota1', 'nota2', 'nota3', 'nota_final']  # Orden en que aparecerán


admin.site.register(Notas,MemberAdmin)
