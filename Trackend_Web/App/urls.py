from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('', views.index, name='index'),
   
   path('login/', views.login_view, name='login'),
   #path('logout/', views.logout_view, name='logout'),
   path('register/', views.register, name='register'),
   path('reset_password/', views.reset, name='reset'),

   
]
