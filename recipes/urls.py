from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='recipes-home'),
    path('recipe/add/', views.add_recipe, name='add-recipes'),
    path('recipe/<int:recipe_id>/', views.detail_view_recipe, name='detail-recipes'),
    path('recipe/<int:recipe_id>/edit', views.edit_recipe, name='edit-recipes'),
    path('recipe/<int:recipe_id>/delete', views.delete_recipe, name='delete-recipes'),
    path('recipes/sort', views.sort_recipe_by_title, name='sort-title'),
    path('recipes/user', views.view_recipes_user, name='user-recipes'),
]
