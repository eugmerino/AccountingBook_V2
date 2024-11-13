from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Company,User
from .forms import companiesForm,usersForm

#Pagina principal de control de empresas
@login_required(login_url="login")
def companyUserView(request):
    all_companies = Company.objects.all()
    all_users = User.objects.all()
    formCompany = companiesForm()
    formUser = usersForm()
    message = ''
    
    if request.method == 'POST':
        formCompany = companiesForm(request.POST)
        formUser = usersForm(request.POST)

        if formCompany.is_valid():
            if not formCompany.isDuplicate:
                formCompany.save()
                formCompany = companiesForm()
                all_companies = Company.objects.all()
                message = "Empresa creada exitosamente!"
            else:
                message = "Ya existe una empresa con ese nombre!"
        
        if formUser.is_valid():
            formUser.save()
            formUser = usersForm()
            all_users = User.objects.all()

            
    objects = {
        "companies":all_companies,
        "formCompany":formCompany,
        "formUser": formUser,
        "message":message,
        "users":all_users
    }
    return render(request,'userMain.html',objects)

# Create your views here.
