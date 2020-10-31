from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Room, Message


def index(request):
    room_list = Room.objects.order_by('-created_at')[:5]
    context = {
        'room_list': room_list,
    }
    return render(request, 'chat/index.html', context)


def chat(request, room_name):
    messages = Message.objects.filter(room__name=room_name).order_by('-created_at')[:50]
    room = Room.objects.get(name=room_name)
    context = {
        'messages': messages,
        'room': room
    }
    return render(request, 'chat/chat_room.html', context)


def room(request):
    name = request.POST.get("room_name")
    Room.objects.create(name=name)
    return redirect('chat:chat_room', room_name=name)
