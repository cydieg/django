from django.shortcuts import render

def headnav(request):
    return render(request, 'themes/headnav.html')

def index(request):
    return render(request, 'themes/index.html')

def login(request):
    return render(request, 'themes/login.html')

def register(request):
    return render(request, 'themes/register.html')

def admin(request):
    return render(request, 'themes/admin.html')

def forgotPass(request):
    return render(request, 'themes/forgotPass.html')

def appointmentAdmin(request):
    return render(request, 'themes/appointmentAdmin.html')


def doctorsAdmin(request):
    return render(request, 'themes/doctorsAdmin.html')

def patientAdmin(request):
    return render(request, 'themes/patientAdmin.html')

def staffAdmin(request):
    return render(request, 'themes/staffAdmin.html')