from django.shortcuts import render, redirect
from django.views.generic import ListView
from jogos.models import Jogo
from jogadores.models import Jogador


class IndexView(ListView):
    template_name = "home/home.html"
    model = Jogo
    context_object_name = "jogos"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["jogadores"] = Jogador.objects.all()
        return context


def administrativo(request):
    return render(request, "administrativo/administrativo.html")
