from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cube_surface_area_calculator/', views.cube_surface_area_calculator, name='cube_surface_area_calculator'),
]
