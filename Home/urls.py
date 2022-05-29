from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contect, name='contect'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('login/', views.login, name='login'),
]
