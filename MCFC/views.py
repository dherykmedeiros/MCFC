from django.shortcuts import render,redirect
from jogos.views import JogoListView
from jogadores.views import JogadorListView


def home(request):
  return render(request,'home/home.html')