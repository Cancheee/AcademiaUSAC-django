"""
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Init import views
from Cursos import views
from Usuarios import views
from django.contrib.auth import views as auth_views
 

urlpatterns = [
    path('admin/', admin.site.urls, name="Administracion"),
    path('', include('Init.urls')),
    path('cursos/', include('Cursos.urls')),
    path('inicio-sesion/', include('Usuarios.urls')),
   #path('inicio/', views.Inicio)
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)