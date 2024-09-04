from django.db import models
from django.contrib.auth.models import AbstractUser

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
    company = models.ForeignKey(Company,
        on_delete = models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Empresa",
    )

    