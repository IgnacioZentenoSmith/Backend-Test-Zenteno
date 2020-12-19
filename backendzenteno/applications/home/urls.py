from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/index', views.indexView.as_view()),
]