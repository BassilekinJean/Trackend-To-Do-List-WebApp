from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
   path('', views.index, name='index'),
   path('index_1/',views.index_1,name='index_1'),
   
   # path('login/', views.login_view, name='login'),
   #path('logout/', views.logout_view, name='logout'),
   path('register/', views.register, name='register'),
   # path('reset_password/', views.reset, name='reset'),
   path('connexion/',auth_views.LoginView.as_view(template_name = 'login.html'),name='login'),
   path('deconnexion/',auth_views.LogoutView.as_view(next_page ='home'),name ='deconnexion'),
   path('reset_password/', auth_views.PasswordResetView.as_view(template_name='forgot-password.html'), name='reset_password'),
]
