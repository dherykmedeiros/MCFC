from django.shortcuts import render
from .models import Jogo, Presenca
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class JogoListView(ListView):
  model = Jogo
  template_name = 'jogos/jogos.html'
  context_object_name = 'jogos'
  paginate_by = 10
  ordering = '-data_jogo'
  queryset = Jogo.objects.all()

class JogoDetailView(DetailView):
  model = Jogo
  template_name = 'jogos/jogo.html'
  pk_url_kwarg = 'id'
  context_object_name = 'jogo'
  
class JogoCreateView(CreateView):
  model = Jogo
  fields = '__all__'
  template_name = 'jogos/cadastrar_jogo.html'
  success_url = reverse_lazy('jogos')

class JogoUpdateView(UpdateView):
  model = Jogo
  fields = '__all__'
  template_name = 'jogos/atualizar_jogo.html'
  pk_url_kwarg = 'id'
  success_url = reverse_lazy('jogos')

class JogoDeleteView(DeleteView):
  model = Jogo
  template_name = 'jogos/deletar_jogo.html'
  pk_url_kwarg = 'id'
  success_url = reverse_lazy('jogos')

