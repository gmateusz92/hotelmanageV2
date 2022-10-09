from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import NewUser

class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(max_length=60, help_text='Requried. Add a valide email adress')

    class Meta:
        model = NewUser
        fields = ['email', 'user_name']