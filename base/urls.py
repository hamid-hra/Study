from django.urls import path
from . import views


urlpatterns = [
    path('',views.home , name='Home'),
    path('room/<str:pk>/',views.room ,name='Room'),
    path('create-room/',views.createRoom,name="create-room"),
]