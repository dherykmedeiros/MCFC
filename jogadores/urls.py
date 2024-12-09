from django.urls import path
from .views import JogadorListView, CreateJogadorView, UpdateJogadorView, DeleteJogadorView, DetailJogadorView

urlpatterns = [
    path('',JogadorListView.as_view(), name='jogadores'),
    path('criar/',CreateJogadorView.as_view(), name='cadastrar_jogador'),
    path('atualizar/<uuid:id>',UpdateJogadorView.as_view(), name='atualizar_jogador'),
    path('detalhes/<uuid:id>',DetailJogadorView.as_view(), name='detalhe_jogador'),
    path('deletar/<uuid:id>',DeleteJogadorView.as_view(), name='deletar_jogador'),
]
