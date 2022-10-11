from . import views
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),

    path('register_user/', views.register_user, name='register_user'),
    path('register_superuser/', views.register_superuser, name='register_superuser'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout_view'),

    path('book/', views.book, name='book'),
    path('booked_rooms/', views.booked_rooms, name='booked_rooms'),
    path('<uuid:room_pk>/', views.room_detail_view, name='room_detail_view'),
    ]
