from django.urls import path
from . import views # Import the views from the admin app
# from django.contrib.auth import views as auth_view

urlpatterns = [
    
]


urlpatterns = [
    path('/dashboard', views.dashboard,name="dashboard"),
    path('login/', views.user_login, name='login_treat'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.user_signup, name='signup'),
    path('password-reset/', views.password_reset_request, name='password_reset'),
    path('password-reset/done/', views.password_reset_done, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('reset/done/', views.password_reset_complete, name='password_reset_complete'),
]