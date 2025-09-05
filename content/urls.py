from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('servicios/', views.services, name='services'),
    path('proyectos/', views.projects, name='projects'),
    path('proyectos/<int:project_id>/', views.project_detail, name='project_detail'),
    path('equipo/', views.team, name='team'),
    path('acerca/', views.about, name='about'),
    path('contacto/', views.contact, name='contact'),
]