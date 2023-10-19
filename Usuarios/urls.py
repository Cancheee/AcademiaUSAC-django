
from django.contrib import admin
from django.urls import path, include
from Usuarios import views
from django.contrib.auth import views as auth_views
from Usuarios.views import Registro

urlpatterns = [
    path('', views.iniciar_sesion, name="inicio-sesion"),
    path('registro', Registro.as_view(), name='registro'),
    path('cerrar_sesion', views.cerrar_sesion, name='cerrar-sesion'),
    # path('registro/', views.registro , name="registro"),
    path('registro-exitoso/', views.registro_exitoso , name="registro_exitoso"),
    path('perfil/', views.perfil , name="perfil"),
    path('accounts/', include('django.contrib.auth.urls')),
    # Añadidos
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="ResetPassword/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="ResetPassword/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="ResetPassword/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="ResetPassword/password_reset_complete.html"), name="password_reset_complete"),
    
]