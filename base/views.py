from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import response
from django.http import HttpResponse 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login ,logout
from .models import Room , Topic
from .forms import RoomForm



def loginPage(request):

      page = 'login'

      if request.user.is_authenticated:
            return redirect('Home')

      if request.method == 'POST':
            username = request.POST.get('username').lower()
            password = request.POST.get('password')
            try:
                  user = User.objects.get(username=username)
            except:
                  messages.error(request ,'user does not exist')

            user = authenticate(request ,username=username , password=password)
            if user is not None:
                  login(request, user)
                  return redirect ('Home')
            else:
                  messages.error(request, 'user name or password does not exits')

      context = {'page' : page}
      return render(request,'login_register.html', context )




def logoutUser(request):
      logout(request)
      return redirect('Home')


def registerPage(request):
      page = 'register'
      form = UserCreationForm()
      if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                  user = form.save(commit=False)
                  user.username = user.username.lower()
                  user.save()
                  login(request,user)
                  return redirect('Home')
            else:
                  messages.error(request, 'An error occurred during registeration')
      context = {'form' : form}
      return render(request, 'login_register.html', context)


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
          Q(topic__name__icontains=q) |
          Q(name__icontains=q) |
          Q(description__icontains=q)
      )
    topics = Topic.objects.all()

    room_count = rooms.count()

    context = {'rooms' : rooms , 'topics' : topics , 'room_count' : room_count}
    return render(request , 'home.html',context)



def room(request,pk):
        room = Room.objects.get(id=pk)
        context = {'room' : room}
        return render(request , 'room.html' , context)




@login_required(login_url='login')
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



@login_required(login_url='login')
def updateRoom(request,pk):
      room = Room.objects.get(id=pk)
      form = RoomForm(instance=room)
      
      if request.user != room.host :
            return HttpResponse('you are not allowed here !!')

      if request.method == 'POST':
            form = RoomForm(request.POST ,instance=room)
            if form.is_valid():
                  form.save()
                  return redirect('Home')
      context = {'form' : form}
      return render (request,'room_form.html',context)






@login_required(login_url='login')
def deleteRoom(request,pk):

      if request.user != room.host :
       return HttpResponse('you are not allowed here !!')

      room = Room.objects.get(id=pk)
      if request.method == 'POST':
            room.delete()
            return redirect('Home')
      return render(request ,'delete.html',{'obj' : room} )