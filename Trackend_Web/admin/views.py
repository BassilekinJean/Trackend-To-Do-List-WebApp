from django.shortcuts import render

#Introduction
# /views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .forms import SignUpForm

# Vue pour la page de connexion
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirection vers la page d'accueil
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    return render(request, 'login.html')

# Vue pour la déconnexion
@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

# Vue pour l'inscription
def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Connecte automatiquement l'utilisateur après inscription
            return redirect('home')  # Redirection vers la page d'accueil
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

# Vue pour demander la réinitialisation de mot de passe
def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            users = User.objects.filter(email=email)
            if users.exists():
                user = users[0]
                subject = "Réinitialisation de votre mot de passe"
                email_template_name = "forgot-password.html"
                c = {
                    "email": user.email,
                    'domain': '127.0.0.1:8000',  # Remplacez par votre domaine
                    'site_name': 'GP',
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "user": user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                }
                #email_content = render_to_string(email_template_name, c)
                #send_mail(subject, email_content, DEFAULT_FROM_EMAIL, [user.email])
                return redirect('password_reset_done')
    else:
        form = PasswordResetForm()
    return render(request, 'forgot-password.html', {'form': form})

# Vue pour confirmer la réinitialisation de mot de passe
def password_reset_confirm(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                return redirect('password_reset_complete')
        else:
            form = SetPasswordForm(user)
        return render(request, 'forgot-password.html', {'form': form})
    else:
        return redirect('password_reset_complete')

# Vue pour confirmer que le mot de passe a été réinitialisé
def password_reset_complete(request):
    return render(request, 'forgot-password.html')

def password_reset_done(request):
    return render(request, 'forgot-password.html')

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')
