from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('add/', views.add, name='add'),
    path('insertar/', views.insertar, name='insertar'),
    path('recuperar/', views.recuperar, name='recuperar'),
    path('cambiar_password/', views.cambiar_pass, name='cambiar_password'),
    path('<int:libro_id>/', views.edit, name='edit'),
    path('add_review/', views.add_review, name='add_review'),
]