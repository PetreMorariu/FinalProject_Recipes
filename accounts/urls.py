from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import login_view,logout_view


urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    # path('logout/', LogoutView.as_view(), name='logout'),

]