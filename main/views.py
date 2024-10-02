from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout,get_user
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

# Arranque del sistemas
def start(request):
    if request.method == 'POST':
        return redirect('login')
    return render(request,'start.html')

# Inicio de sesión
def loginView(request):
    mensaje = ""
    if request.method == 'POST':
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            mensaje = "Usuario o contraseña invalido"

    objects = {"form" : forms.myAuthenticationForm,
               "mensaje" : mensaje}
    return render(request,'login.html',objects)

# Dashboard
@login_required(login_url="/login")
def dashboard(request):
    return render(request,'dashboard.html')
