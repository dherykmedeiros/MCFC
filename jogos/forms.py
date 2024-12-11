from django import forms
from .models import DesempenhoJogador

class DesempenhoJogadorForm(forms.ModelForm):
  class Meta:
    model = DesempenhoJogador
    fields = ['jogador', 'gols', 'assistencias', 'mvp', 'clean_sheet']

  def __init__(self, *args,jogadores_confirmados=None ,**kwargs ):
    super().__init__(*args, **kwargs)
    if jogadores_confirmados is not None:
      self.fields['jogador'].queryset = jogadores_confirmados