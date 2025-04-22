from django.urls import path
from django.contrib.auth.views import LogoutView
from accounts import views


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    # path('logout/', LogoutView.as_view(), name='logout'),
]