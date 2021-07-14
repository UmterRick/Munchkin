from django.http import response
from django.http.response import Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect, resolve_url
from django.http import HttpResponse
from .models import Game, Player
from uuid import uuid4


def home(request):
    return render(request, 'home.html')


def clear_cookie(request):
    request.session['room_id'] = ''
    response = redirect('new_room')
    new_room(request)
    return response


def new_room(request):
    old_room_id = request.session.get('room_id')
    players = Player.objects.filter(game_id=old_room_id)
    if old_room_id != '':
        return render(request, 'new_game.html', {'room_id': old_room_id, 'players': players})
    room_id = uuid4()
    Game.objects.create(myid=room_id, status=0)
    request.session['room_id'] = str(room_id)
    return render(request, 'new_game.html', {'room_id': request.session.get('room_id'),  'players': players})


def join_room(request):
    print("Join Room...")
    return render(request, 'join_room.html')


def new_player(request):
    if request.method == "POST":
        print(request.POST)
        if 'name_input' in request.POST:
            name = request.POST.get('name_input')

            game_id = request.POST.get('id_input')
            game = Game.objects.get(pk=game_id)
            new_player = Player(myid=str(uuid4()), name=name,game=game, status='Wait')
            new_player.save()
            return render(request, 'join_room.html')
    return HttpResponse(f"Your name is {request.GET.get('apply_Name')}")


def check_name(request, *args, **kwargs):
    name = request.GET.get('name')
    duplicates_name = Player.objects.filter(name=name)
    print(f'{duplicates_name=}')
    if not duplicates_name:
        return JsonResponse({'data': True})
    return JsonResponse({'data': True})

def validate_player(request):
    player_name = request.POST.get('name')
    game_room = request.POST.get('game_id')
    data = {
        'name' : False,
        'game_id': False}
    if len(game_room) == 36:
        data['game_id'] = True
    if len(player_name) > 3:
        data['name'] = True
    return JsonResponse(data)

