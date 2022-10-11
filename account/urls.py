from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),

    path('register_user/', views.register_user, name='register_user'),
    path('register_superuser/', views.register_superuser, name='register_superuser'),
    #path('logout/', views.logout, name='logout'),

   # path('room_detail_view/', views.room_detail_view, name='room_detail_view')
   path('<uuid:room_pk>/', views.room_detail_view, name='room_detail_view'),
    ]
