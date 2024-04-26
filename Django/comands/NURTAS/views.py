from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Player
from .forms import PlayerForm


def delete_player(request, id):
    player = get_object_or_404(Player, id=id)
    if request.method == 'POST':
        player.delete()
        return redirect('players')
    return render(request, 'NURTAS/delete_player.html', {'player': player})


def add_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('players')  # Перенаправление на страницу всех команд
    else:
        form = PlayerForm()
    return render(request, 'NURTAS/add_player.html', {'form': form})


def edit_player(request, id):
    player = get_object_or_404(Player, id=id)
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('teams')  # Перенаправление на страницу всех команд после успешного редактирования
    else:
        form = PlayerForm(instance=player)
    return render(request, 'NURTAS/edit_player.html', {'form': form})



def index(request):
    return render(request, 'NURTAS/index.html')

def players(request):
    players = Player.objects.all()  # Получение всех игроков из базы данных
    return render(request, "NURTAS/players.html", {'players': players})


def details(request, id):
    player = Player.objects.get(id=id)
    return render(request, "NURTAS/details.html", {'team': player})

def details(request, id):
    team = Player.objects.get(id=id)
    template = loader.get_template("NURTAS/details.html")
    context = {
        "team": team
    }
    return HttpResponse(template.render(context=context))


