from django.shortcuts import render

def gamin(request):
    return render(request, 'game\game_all.html')
