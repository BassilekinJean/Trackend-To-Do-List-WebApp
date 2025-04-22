from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from .views import *

urlpatterns = [
   path('', views.index, name='index'),
]
