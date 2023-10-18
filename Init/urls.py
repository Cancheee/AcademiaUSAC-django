from django.contrib import admin
from django.urls import path, include
from Init import views


urlpatterns = [
    path('', views.inicio, name="inicio"),
]
