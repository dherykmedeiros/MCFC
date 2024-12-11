from django.urls import path
from .views import JogoCreateView, JogoListView, JogoDetailView, JogoDeleteView, JogoUpdateView, PresencaListView,MarcarPresencaView, EditarPresencaView
from django.contrib.auth.decorators import login_required,user_passes_test

def is_admin(user):
  return user.groups.filter(name='administrativo').exists()

urlpatterns = [
    path('',JogoListView.as_view(),name='jogos'),
    path('criar/',login_required(user_passes_test(is_admin)(JogoCreateView.as_view())),name='criar_jogo'),
    path('detalhe/<uuid:id>',JogoDetailView.as_view(),name='jogo'),
    path('atualizar/<uuid:id>',login_required(user_passes_test(is_admin)(JogoUpdateView.as_view())),name='atualizar_jogo'),
    path('deletar/<uuid:id>',login_required(user_passes_test(is_admin)(JogoDeleteView.as_view())),name='deletar_jogo'),
    path('presencas/<uuid:jogo_id>' ,login_required(PresencaListView.as_view()), name='presencas' ),
    path('marcar_presenca/<uuid:jogo_id>',login_required(MarcarPresencaView.as_view()),name='marcar_presenca'),
    path('editar_presenca/<uuid:presenca_id>/',login_required(EditarPresencaView.as_view()), name='editar_presenca')
]
