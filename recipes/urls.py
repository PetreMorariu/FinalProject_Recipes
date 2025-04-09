from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='recipes-home'),
    path('about/', views.about, name='recipes-about'),
    path('recipe/add/', views.add_recipe, name='add-recipes'),
    path('recipe/<int:recipe_id>/edit', views.edit_recipe, name='edit-recipes'),
    path('recipe/<int:recipe_id>/', views.detail_view_recipe, name='detail-recipes'),
]
