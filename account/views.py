from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm

from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Accounts
from django.contrib import messages, auth


def home(request):
    return render(request, 'home.html')

#def register(request):
    # context = {}
    # if request == "POST":
    #     form = RegistrationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         email = form.cleaned_data.get('email')
    #         raw_password = form.cleaned_data.get('password1')
    #         account = authenticate(email=email, password=raw_password)
    #         login(request, account)
    #         return redirect('home')
    #     else:
    #         context['registration_form'] = form
    # else:
    #     form = RegistrationForm()
    #     context['registration_form'] = form
    # return render(request, 'register_superuser.html', context)
    form = RegistrationForm
    #context = {'form': form }
   # return render(request, 'register_superuser.html', context)


def register_user(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid(): #jezeli dane sa prawidlowe
            first_name = form.cleaned_data['first_name'] #cleaned_data pobiera dane z formularza
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number'] #w modelu nie ma phone_number dlatego nie djamye tego w user = account.
            email = form.cleaned_data['email']
            username = email.split("@")[0] #nie tworzymy username
            password = form.cleaned_data['password']
            #confirm_password = form.cleaned_data['confirm_password']
            user = Accounts.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password,) #create_user bierze sie z models
            user.phone_number = phone_number
            user.save()
            # if password != confirm_password:
            #     return redirect('home')
            messages.success(request, 'Registration succesfull.')
            return redirect('register_user')
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'register_user.html', context)

def register_superuser(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid(): #jezeli dane sa prawidlowe
            first_name = form.cleaned_data['first_name'] #cleaned_data pobiera dane z formularza
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number'] #w modelu nie ma phone_number dlatego nie djamye tego w user = account.
            email = form.cleaned_data['email']
            username = email.split("@")[0] #nie tworzymy username
            password = form.cleaned_data['password']
            #confirm_password = form.cleaned_data['confirm_password']
            user = Accounts.objects.create_superuser(first_name=first_name, last_name=last_name, email=email, username=username, password=password,) #create_user bierze sie z models
            user.phone_number = phone_number
            user.save()
            # if password != confirm_password:
            #     return redirect('home')
            messages.success(request, 'Registration succesfull.')
            return redirect('register_superuser')
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'register_superuser.html', context)
