from django.shortcuts import render

# Create your views here.
def dashboard():
    return render('templates/dashboard.html')