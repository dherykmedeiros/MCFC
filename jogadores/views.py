from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from .models import Jogador
from django.urls import reverse_lazy

# Create your views here.

class JogadorListView(ListView):
  model = Jogador
  template_name = "jogadores/jogadores.html"
  context_object_name = "jogadores"

class CreateJogadorView(CreateView):
  model = Jogador
  template_name = "jogadores/cadastrar_jogador.html"
  fields = '__all__'
  context_object_name = "cadastrar_jogador"
  success_url = reverse_lazy('jogadores')


class DetailJogadorView(DetailView):
  model = Jogador
  template_name = "jogadores/jogador.html"
  context_object_name = "jogador"

class UpdateJogadorView(UpdateView):
  model = Jogador
  fields = '__all__'
  template_name = "jogadores/atualizar_jogador.html"
  context_object_name = "atualizar_jogador"
  success_url = reverse_lazy('jogadores')

class DeleteJogadorView(DeleteView):
  model = Jogador
  template_name = "jogadores/delete_jogador.html"
  context_object_name = "deletar_jogador"
  success_url = reverse_lazy('jogadores')