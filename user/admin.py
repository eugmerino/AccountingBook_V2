from django.contrib import admin
from .models import User
from .models import Company

# Register your models here.
admin.site.register(User)

@admin.register(Company)
class Company(admin.ModelAdmin):
    list_display = ('name',)