from django.db import models
from django.contrib.auth.models import AbstractUser,Group
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_migrate
from django.dispatch import receiver



# Create your models here.

class Company(models.Model):
    """
    Representa la información de una empresa
    """
    name=models.CharField("Empresa", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Empresa"
        verbose_name_plural="Empresas"

class User(AbstractUser):
    """
    Representa un usuario del sistema heredando del que crea django y agregandole un campo
    """
    company = models.ForeignKey(Company,
        on_delete = models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Empresa",
    )

class Period(models.Model):
    """
    Representa un ciclo contable de una empresa
    """
    year = models.IntegerField("Año",
        validators=[MinValueValidator(2000), MaxValueValidator(2050)]
    );
    company = models.ForeignKey(Company,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Empresa"
    )
    isOpen = models.BooleanField("Ciclo abierto",default=True)
    description = models.CharField("Descripción del periodo",max_length=250)


    def __str__(self):
        return self.company.name+" "+str(self.year)
    class Meta:
        verbose_name="Periodo"
        verbose_name_plural="Periodos"


@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    """
    Crea grupos predeterminados después de que se completen las migraciones.
    """
    groups = ['Gerente', 'Auditor', 'Contador']
    
    for group_name in groups:
        Group.objects.get_or_create(name=group_name)
    print("Grupos predeterminados creados (si no existían).")