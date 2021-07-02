from django.http.response import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Game
from uuid import uuid4
# Create your views here.


def home(request):
    return render(request, 'home.html')


def new_room(request, pk):
    games = get_object_or_404(Game, pk=pk)
    return render(request, 'new_game.html', {'games': games})


def join_room(request):
    print("Join Room...")

    return render(request, 'join_room.html')
