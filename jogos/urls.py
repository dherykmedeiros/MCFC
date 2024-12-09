from django.urls import path
from .views import JogoCreateView, JogoListView, JogoDetailView, JogoDeleteView, JogoUpdateView

urlpatterns = [
    path('',JogoListView.as_view(),name='jogos'),
    path('criar/',JogoCreateView.as_view(),name='criar_jogo'),
    path('detalhe/<int:pk>',JogoDetailView.as_view(),name='jogo'),
    path('atualizar/<int:pk>',JogoUpdateView.as_view(),name='atualizar_jogo'),
    path('deletar/<int:pk>',JogoDeleteView.as_view(),name='deletar_jogo'),
]
