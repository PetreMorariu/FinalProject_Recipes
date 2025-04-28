from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='recipes-home'),
    path('recipes/add/', views.add_recipe, name='add-recipes'),
    path('recipes/<int:recipe_id>/', views.detail_view_recipe_v2, name='detail-recipes'),
    path('recipes/<int:recipe_id>/edit/', views.edit_recipe, name='edit-recipes'),
    path('recipes/<int:recipe_id>/delete/', views.delete_recipe, name='delete-recipes'),
    path('recipes/sort_title/', views.sort_recipe_by_title, name='sort-title'),
    path('recipes/sort_date/', views.sort_recipe_by_date, name='sort-date'),
    path('recipes/user/', views.view_recipes_user, name='user-recipes'),
    path('recipes/search/', views.search, name='search-recipes'),
    path('recipes/<int:recipe_id>/comment/', views.add_comment, name='comment-recipes'),
]
