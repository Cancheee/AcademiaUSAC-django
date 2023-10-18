from django.contrib import admin
from .models import Estudiantes, Catedraticos


class EstudiantesAdmin(admin.ModelAdmin):
    list_display=('usuario', 'nombre', 'apellido', 'dpi', 'correo')
    search_fields=('usuario', 'nombre', 'apellido', 'dpi', 'correo')
    
admin.site.register(Estudiantes, EstudiantesAdmin)

# class EstudiantesAdmin(admin.ModelAdmin):
#     list_display = ('usuario', 'nombre', 'apellido', 'correo', 'telefono', 'dpi', 'fecha_nacimiento', 'imagen', 'is_active')
#     search_fields = ['usuario']
#     list_per_page = 20  # Opcional: para especificar cuántos registros se muestran por página en el administrador

# admin.site.register(Estudiantes, EstudiantesAdmin)

class CatedraticossAdmin(admin.ModelAdmin):
    list_display=('nombre', 'apellido', 'DPI')
    search_fields=('nombre', 'apellido', 'DPI')

admin.site.register(Catedraticos, CatedraticossAdmin)