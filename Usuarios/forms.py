from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Estudiantes

# Nuevo
class EstudiantesForm(forms.ModelForm):
    class Meta:
        model = Estudiantes
        fields = '__all__'  # Esto incluirá todos los campos del modelo en el formulario

        widgets={'birthdate': forms.DateInput(attrs={'type':'date'}),  
         #         'contraseña': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
        #         'contraseña': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
        #         'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña (Confirmacion)'})
        }  

class EstudianteRegistroForm(UserCreationForm):
    class Meta:
        model = Estudiantes
        fields = ['nombre', 'apellido', 'fecha_nacimiento','dpi', 'telefono','imagen', 'usuario', 'correo','password1','correo',  ]

class UserRegisterForm(UserCreationForm):
    
    first_name = forms.CharField(label='Nombre', min_length=3, max_length=15)  
    last_name = forms.CharField(label='Apellido', min_length=3, max_length=15) 
    dpi = forms.IntegerField(label='DPI')
    fecha_de_nacimiento=forms.DateField()
    telefono=forms.CharField()
    email=forms.EmailField()
    password1=forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='Contraseña (Confirmacion)', widget=forms.PasswordInput)
    
    # profile_image = forms.ImageField(label='Foto de perfil')

    class Meta:
        model=User
        fields=['first_name', 'last_name','dpi', 'fecha_de_nacimiento', 'telefono','username','email','password1','password2']
        # help_texts={k:"" for k in fields}