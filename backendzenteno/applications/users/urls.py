from django.urls import path
from . import views

app_name = "users_app"

urlpatterns = [
    path(
        'users/register', 
        views.UserRegisterView.as_view(),
        name='user-register',
    ),
    path(
        'users/login', 
        views.LoginUser.as_view(),
        name='user-login',
    ),
    path(
        'users/logout', 
        views.LogoutView.as_view(),
        name='user-logout',
    ),
    path(
        'users/profile/<pk>', 
        views.UserUpdateView.as_view(),
        name='user-profile',
    ),
]