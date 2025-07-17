from django.urls import path
from . import views


urlpatterns = [
    path('login', views.loginPage, name="login"),
    path('register', views.registerPage, name="register"),
    path('logout',views.logoutUser, name='logout'),
    path('',views.home , name='Home'),
    path('room/<str:pk>/',views.room ,name='Room'),
    path('create-room/',views.createRoom,name="create-room"),
    path('Upadte-room/<str:pk>/',views.updateRoom,name="Update-room"),
    path('delete-room/<str:pk>/',views.deleteRoom,name="Delete-room"),
    path('delete-message/<str:pk>/',views.deleteMessage,name="Delete-message"),
]   