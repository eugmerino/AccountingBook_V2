from django import forms
from .models import Company,User,Period

class companiesForm(forms.ModelForm):
    """
        Creación de empresas (No se ocupa)
    """
    class Meta:
        model = Company
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}) 
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Company.objects.filter(name=name).exists():
            raise forms.ValidationError("Ya existe una empresa con ese nombre!")
        return name
    
class usersForm(forms.ModelForm):
    """
        Creación de usuarios (tomando como base la compañia del usuario en sesión)
    """
    class Meta:
        model= User
        fields = ['username','password','email','first_name','last_name','groups']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}), 
            'first_name': forms.TextInput(attrs={'class': 'form-control'}), 
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'groups': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_groups(self):
        groups = self.cleaned_data['groups']
        if len(groups) != 1:  # Permitir solo un grupo
            raise forms.ValidationError("Debe seleccionar un solo grupo.")
        return groups

    def __init__(self, *args, company=None, **kwargs):
        super(usersForm, self).__init__(*args, **kwargs)
        self.fields['groups'].required = True
        self.fields['email'].required = True
        self.company = company

    def save(self, commit=True):
        user = super(usersForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if self.company:
            user.company = self.company

        if commit:
            user.save()
            # Si hay grupos, añadirlos al usuario después de guardarlo
            self.save_m2m()
        return user

class periodForm(forms.ModelForm):
    """
        Creación de periodos (tomando en cuenta la compañia del usuario en sesión)
    """
    class Meta:
        model = Period
        fields = ['year', 'description', 'isOpen']
        widgets = {
            'year': forms.NumberInput(attrs={'class':'form-control'}),
            'isOpen': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
        }

    def __init__(self, *args, company=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company

    def clean_year(self):
        year = self.cleaned_data.get('year')
        
        
        if self.company and Period.objects.filter(company=self.company, year=year).exists():
            raise forms.ValidationError(f"La compañía ya tiene un registro para el año {year}.")
        
        return year

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.company:
            instance.company = self.company
        if commit:
            instance.save()
        return instance

    
