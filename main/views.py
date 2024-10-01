from django.shortcuts import render,redirect

# Create your views here.
def start(request):
    if request.method == 'POST':
        return redirect('login/')
    return render(request,'start.html')

def login(request):
    return render(request,'login.html')