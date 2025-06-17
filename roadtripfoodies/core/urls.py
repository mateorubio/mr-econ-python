from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('receta/nueva/', views.nueva_receta, name='nueva_receta'),
    path('autor/nuevo/', views.nueva_autor, name='nueva_autor'),
    path('destino/nuevo/', views.nuevo_destino, name='nuevo_destino'),
]