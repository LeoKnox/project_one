from django.shortcuts import render, get_object_or_404
from .models import Room

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room/list.html', {'rooms': rooms})