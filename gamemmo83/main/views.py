from django.shortcuts import render
from games.models import Gamelist

def index(request):
    games = Gamelist.objects.all()[1:3]
    return render(request, 'main/index.html', {'games':games})
