from django  import forms
from django.contrib.auth.forms import AuthenticationForm

# Devuelve el formulario para inicio de sesión
class myAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.widgets.TextInput(attrs={
                'class': 'form-control'
            })
        self.fields['password'].widget = forms.widgets.PasswordInput(attrs={
                'class': 'form-control'
            })