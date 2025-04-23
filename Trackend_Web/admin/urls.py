from django.urls import path
from . import views # Import the views from the admin app
# from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.dashboard,name="dashboard"),
]