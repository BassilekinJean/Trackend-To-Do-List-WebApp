from django.shortcuts import render
from .forms import *
from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from os import *
from .forms import InstriptionForm
from django.contrib import messages

# Create your views here.

def index(request):

    return render(request, 'index.html')

def index_1(request):

    return render(request, 'index-1.html')

def login_view(request):
    return render(request, 'login.html')

# def register(request):
#     return render(request, 'register.html')

# def register(request):
#     form = InstriptionForm(request.POST)
#     if request.method == 'POST':
#         if form.is_valid():
#             user = form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request,f'compte cree pour { username }.vous pouvez maintenant vous connecter.')
#             return redirect('connexion')
#         else:
#             form = InstriptionForm()
#     return render(request,'register.html',{'form':form})

def register(request):
    if request.method == "POST":
        form = InstriptionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Compte créé avec succès.")
            return redirect('login')
    else:
        form = InstriptionForm()

    return render(request, 'register.html', {'form': form})


def reset(request):
    return render(request, 'forgot-password.html')

