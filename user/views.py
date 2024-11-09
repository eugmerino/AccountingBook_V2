from django.shortcuts import render

#Pagina principal de empleados
def userMainView(request):
    return render(request,'userMain.html')

# Create your views here.
