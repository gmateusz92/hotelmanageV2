from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm

from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Accounts
from django.contrib import messages, auth
from .models import Room, RoomStatus, RoomType

def home(request):
    rooms = Room.objects.all()#.filter(is_active=True)
    room_status = RoomStatus.objects.all()
    count_all = rooms.count()
    count_available = room_status.count()

    context = {'rooms': rooms,
               'count_available': count_available,
               'count_all': count_all,
               'room_status': room_status}
    return render(request, 'home.html', context)

def room_detail_view(request, room_pk):
    room_detail = get_object_or_404(Room, pk=room_pk) #mozna dawać room_pk albo room_id
    context = {'room_detail': room_detail}
    return render(request, 'rooms/room_detail_view.html', context)

# def show_1person:
#     pass

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
