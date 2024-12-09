from django.urls import path
from .views import JogoCreateView, JogoListView, JogoDetailView, JogoDeleteView, JogoUpdateView

urlpatterns = [
    path('',JogoListView.as_view(),name='jogos'),
    path('criar/',JogoCreateView.as_view(),name='criar_jogo'),
    path('detalhe/<uuid:id>',JogoDetailView.as_view(),name='jogo'),
    path('atualizar/<uuid:id>',JogoUpdateView.as_view(),name='atualizar_jogo'),
    path('deletar/<uuid:id>',JogoDeleteView.as_view(),name='deletar_jogo'),
]
