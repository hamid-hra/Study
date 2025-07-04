from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
# rooms = [
#     {'id' : 1 , 'name' : 'Hamid reza atari'},
#     {'id': 2 , "name":"mohammad amin Atari"},
#     {'id': 3 , 'name': "amir hesam atari"}

# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms' : rooms}
    return render(request , 'home.html',context)

def room(request,pk):
        room = Room.objects.get(id=pk)
        context = {'room' : room}
        return render(request , 'room.html' , context)

def createRoom(request):
      context = {}
      return render (request,'room_form.html',context)