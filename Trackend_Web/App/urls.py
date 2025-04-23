from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('', views.index, name='index'),
   path('connexion/',auth_views.LoginView.as_view(template_name = 'login.html'),name='login'),
   path('deconnexion/',auth_views.LogoutView.as_view(next_page ='index'),name ='deconnexion'),
   # path('inscription/',inscription,name='inscription'),
]
