from django import forms
from .models import Company,User

class companiesForm(forms.ModelForm):
    isDuplicate = False
    class Meta:
        model = Company
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})  # Aquí agregas la clase de Bootstrap
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Company.objects.filter(name=name).exists():
            self.isDuplicate = True
        return name
    
class usersForm(forms.ModelForm):
    class Meta:
        model= User
        fields = ['username','password','first_name','last_name','company','groups']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}), 
            'first_name': forms.TextInput(attrs={'class': 'form-control'}), 
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.Select(attrs={'class': 'form-select'}),
            'groups': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }
