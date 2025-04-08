from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='recipes-home'),
    path('about/', views.about, name='recipes-about'),
    path('recipe/add/', views.add_recipe, name='add-recipes'),
]
