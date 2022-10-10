from django.contrib import admin
from .models import Accounts
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea


# class UserAdminConfig(UserAdmin):
#     model = Account
#     search_fields = ('email', 'user_name', 'first_name',)
#     list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff')
#     ordering = ('-start_date',)
#     list_display = ('email', 'user_name', 'first_name',
#                     'is_active', 'is_staff')
#     fieldsets = (
#         (None, {'fields': ('email', 'user_name', 'first_name',)}),
#         ('Permissions', {'fields': ('is_staff', 'is_active')}),
#         ('Personal', {'fields': ('about',)}),
#     )
#     formfield_overrides = {
#         Account.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
#     }
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')}
#          ),
#     )
class AccountAdmin(UserAdmin): #do tego zeby nie dalo sie edytowac hasla wpanelu admina
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active' )#zeby wywietlalo sie przy emailu
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Accounts, AccountAdmin)