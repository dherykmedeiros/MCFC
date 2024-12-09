from django.urls import path
from .views import JogadorListView, CreateJogadorView, UpdateJogadorView, DeleteJogadorView, DetailJogadorView

urlpatterns = [
    path('',JogadorListView.as_view(), name='jogadores'),
    path('criar/',CreateJogadorView.as_view(), name='cadastrar_jogador'),
    path('atualizar/<int:pk>',UpdateJogadorView.as_view(), name='atualizar_jogador'),
    path('detalhes/<int:pk>',DetailJogadorView.as_view(), name='detalhe_jogador'),
    path('deletar/<int:pk>',DeleteJogadorView.as_view(), name='deletar_jogador'),
]
