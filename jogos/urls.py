from django.urls import path
from .views import JogoCreateView, JogoListView, JogoDetailView, JogoDeleteView, JogoUpdateView, PresencaListView,MarcarPresencaView, EditarPresencaView

urlpatterns = [
    path('',JogoListView.as_view(),name='jogos'),
    path('criar/',JogoCreateView.as_view(),name='criar_jogo'),
    path('detalhe/<uuid:id>',JogoDetailView.as_view(),name='jogo'),
    path('atualizar/<uuid:id>',JogoUpdateView.as_view(),name='atualizar_jogo'),
    path('deletar/<uuid:id>',JogoDeleteView.as_view(),name='deletar_jogo'),
    path('presencas/<uuid:jogo_id>' ,PresencaListView.as_view(), name='presencas' ),
    path('marcar_presenca/<uuid:jogo_id>',MarcarPresencaView.as_view(),name='marcar_presenca'),
    path('editar_presenca/<uuid:presenca_id>/',EditarPresencaView.as_view(), name='editar_presenca')
]
