from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import uuid
from django.contrib.auth.models import User


# class CustomAccountManager(BaseUserManager):
#
#     def create_superuser(self, email, user_name, first_name, password, **other_fields):
#
#         other_fields.setdefault('is_staff', True)
#         other_fields.setdefault('is_superuser', True)
#         other_fields.setdefault('is_active', True)
#
#         if other_fields.get('is_staff') is not True:
#             raise ValueError(
#                 'Superuser must be assigned to is_staff=True.')
#         if other_fields.get('is_superuser') is not True:
#             raise ValueError(
#                 'Superuser must be assigned to is_superuser=True.')
#         return self.create_user(email, user_name, first_name, password, **other_fields)
#
#
#     def create_user(self, email, user_name, first_name, password, **other_fields):
#
#         if not email:
#             raise ValueError(_('You must provide an email address'))
#
#         email = self.normalize_email(email)
#         user = self.model(email=email, user_name=user_name,
#                           first_name=first_name, **other_fields)
#         user.set_password(password)
#         user.save()
#         return user
#
#
# class NewUser(AbstractBaseUser, PermissionsMixin):
#
#     email = models.EmailField(_('email address'), unique=True)
#     user_name = models.CharField(max_length=150, unique=True)
#     first_name = models.CharField(max_length=150, blank=True)
#     start_date = models.DateTimeField(default=timezone.now)
#     about = models.TextField(_(
#         'about'), max_length=500, blank=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)
#
#     objects = CustomAccountManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['user_name', 'first_name']
#
#     def __str__(self):
#         return self.user_name

class MyAccountManager(BaseUserManager): #dla superusera
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User must have an email adress')
        if not username:
            raise ValueError('User must have and username')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self.db)
        return user

class Accounts(AbstractBaseUser):  #dla zwyklego uztkownika
    first_name =     models.CharField(max_length=50)
    last_name  =     models.CharField(max_length=50)
    username =       models.CharField(max_length=50, unique=True)
    email =          models.EmailField(max_length=50, unique=True)
    phone_number =   models.CharField(max_length=50)

    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager() # mowimy ze zarządzamy poprzez klase MyAccountManager

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None): #do zapamietania tak musi byc jesli uzytkownik ma prawa admin ma prawo do zmian
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


class RoomType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=30, unique=True)
    price = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'Room {self.type}  person' #price: {self.price}'

class RoomStatus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f' {self.status}'


class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room_type_id = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    room_status_id = models.ForeignKey(RoomStatus, on_delete=models.CASCADE)
    room_no = models.CharField(max_length=5, unique=True)
    price = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'Room {self.room_no} price:{self.price}'

class Book(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Accounts, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Rezerwacja {self.customer_id.first_name} {self.customer_id.last_name}'
#trzeba sprobowac tak jak add cart w ecomreceudemy