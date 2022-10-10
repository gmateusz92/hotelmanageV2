from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),

    path('register_user/', views.register_user, name='register_user'),
    path('register_superuser/', views.register_superuser, name='register_superuser'),
    #path('logout/', views.logout, name='logout'),
    ]
