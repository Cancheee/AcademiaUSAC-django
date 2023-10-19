from django.contrib import admin
from .models import Estudiantes, Catedraticos

class EstudiantesAdmin(admin.ModelAdmin):
    fields=('user','first_name', 'last_name', 'username', 'DPI', 'telefono', 'email', 'login_attempts', 'profile_image')
    readonly_fields=('user','first_name', 'last_name', 'username', 'DPI', 'telefono', 'email', 'login_attempts') #Evitar la modificacion en la edicion de registro
    list_display = ['first_name', 'last_name', 'username', 'email', 'DPI'] #Propiedades visibles del campo
    ordering = ['username']    #Ordena registros por
    search_fields = ['username', 'email'] #Permite buscar por
    # list_display_links = [''] #brindar link a campo
    # list_filter=['']  #Añadir buscar por filtro
    list_per_page=15    #Cantidad de items por pagina
    # exclude=['']      #Excluir campos en la edicion de registro

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