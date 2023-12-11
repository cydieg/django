from django.shortcuts import render

def index(request):
    return render(request, 'themes/index.html')

def login(request):
    return render(request, 'themes/login.html')

def register(request):
    return render(request, 'themes/register.html')

def admin(request):
    return render(request, 'themes/admin.html')
