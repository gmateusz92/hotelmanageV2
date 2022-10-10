from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Accounts

class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(max_length=60, help_text='Requried. Add a valide email adress')

    class Meta:
        model = Accounts
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']