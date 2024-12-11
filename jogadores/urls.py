from django.urls import path
from .views import JogadorListView, CreateJogadorView, UpdateJogadorView, DeleteJogadorView, DetailJogadorView
from django.contrib.auth.decorators import login_required,user_passes_test

def is_admin(user):
  return user.groups.filter(name='administrativo').exists()

urlpatterns = [
    path('',JogadorListView.as_view(), name='jogadores'),
    path('criar/',login_required(user_passes_test(is_admin)(CreateJogadorView.as_view())), name='cadastrar_jogador'),
    path('atualizar/<uuid:id>',login_required(user_passes_test(is_admin)(UpdateJogadorView.as_view())), name='atualizar_jogador'),
    path('detalhes/<uuid:id>',DetailJogadorView.as_view(), name='detalhe_jogador'),
    path('deletar/<uuid:id>',login_required(user_passes_test(is_admin)(DeleteJogadorView.as_view())), name='deletar_jogador'),
]
