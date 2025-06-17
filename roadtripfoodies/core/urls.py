from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('receta/nueva/', views.nueva_receta, name='nueva_receta'),
    path('autor/nuevo/', views.nueva_autor, name='nueva_autor'),
    path('destino/nuevo/', views.nuevo_destino, name='nuevo_destino'),
    path('receta/<int:receta_id>/', views.detalle_receta, name='detalle_receta'),
    path('destino/<int:destino_id>/', views.detalle_destino, name='detalle_destino'),
    path('autor/<int:autor_id>/', views.detalle_autor, name='detalle_autor'),
]