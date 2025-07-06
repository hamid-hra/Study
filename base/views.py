from django.shortcuts import render ,redirect
from django.http import HttpResponse 
from .models import Room , Topic
from .forms import RoomForm

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(topic__name__contains=q)
    topics = Topic.objects.all()

    context = {'rooms' : rooms , 'topics' : topics}
    return render(request , 'home.html',context)

def room(request,pk):
        room = Room.objects.get(id=pk)
        context = {'room' : room}
        return render(request , 'room.html' , context)

def createRoom(request):
      form = RoomForm()
      if request.method == 'POST':
           form = RoomForm(request.POST)
           if form.is_valid():
                form.save()
                return redirect('Home')
           print(request.POST)
      context = {'form' : form}
      return render (request,'room_form.html',context)

def updateRoom(request,pk):
      room = Room.objects.get(id=pk)
      form = RoomForm(instance=room)
      if request.method == 'POST':
            form = RoomForm(request.POST ,instance=room)
            if form.is_valid():
                  form.save()
                  return redirect('Home')
      context = {'form' : form}
      return render (request,'room_form.html',context)

def deleteRoom(request,pk):
      room = Room.objects.get(id=pk)
      if request.method == 'POST':
            room.delete()
            return redirect('Home')
      return render(request ,'delete.html',{'obj' : room} )