from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Estudiantes 

# Nuevo

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    telefono=forms.CharField(max_length=8)
    fecha_nacimiento=forms.DateField()
    dpi = forms.IntegerField(label='DPI')
    profile_image = forms.ImageField(label='Foto de perfil')  # Cambia required a False

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        
        return password2

    def email_clean(self):
        email = self.cleaned_data.get('email')
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError("El email ya está vinculado con otra cuenta, utiliza uno diferente.")
        
        return email