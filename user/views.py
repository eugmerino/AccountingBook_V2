from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Company,User,Period
from .forms import companiesForm,usersForm,periodForm
from django.contrib.auth.models import Group


@login_required(login_url="login")
def companyUserView(request):
    """
        Da acceso al gerente para ver y agregar datos de periodos y usuarios de la empresa que fue asignado
    """
    message = ""

    companyUser = request.user.company

    periodsCompany = Period.objects.filter(company=companyUser)
    usersCompany = User.objects.filter(company=companyUser)

    formPeriod = periodForm(company=companyUser)
    formUser = usersForm(company=companyUser)

    if request.method == 'POST':
        formPeriod = periodForm(request.POST,company=companyUser)

        if formPeriod.is_valid():
            formPeriod.save()
            formPeriod = periodForm(company=companyUser)
            periodsCompany = Period.objects.filter(company=companyUser)
            message = "Periodo creado exitosamente!"
        else:
            message = "Ocurrio un error, ingrese al formulario!"

        formUser = usersForm(request.POST, company=companyUser)

        if formUser.is_valid():
            formUser.save()
            formUser = usersForm(company=companyUser)
            usersCompany = User.objects.filter(company=companyUser)
            message = "Usuario creado exitosamente!"
        else:
            message = "Ocurrio un error, ingrese al formulario de usuario!"

    
    userWithGroups = [
        {
            "user": user,
            "groups": user.groups.all()
        }
        for user in usersCompany
    ]
    

    objects = {
        "company":companyUser,
        "periods":periodsCompany,
        "users":userWithGroups,
        "formPeriod":formPeriod,
        "formUser":formUser,
        "message":message,
    }
    return render(request, 'userMain.html', objects)


# Create your views here.
