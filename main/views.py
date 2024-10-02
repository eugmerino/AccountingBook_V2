from django.shortcuts import render,redirect
from . import forms

# Create your views here.
def start(request):
    if request.method == 'POST':
        return redirect('login/')
    return render(request,'start.html')

def login(request):
    objects = {"form" : forms.myAuthenticationForm}
    return render(request,'login.html',objects)