from django import forms
from .models import DesempenhoJogador

class DesempenhoJogadorForm(forms.ModelForm):
    class Meta:
        model = DesempenhoJogador
        fields = ['jogador', 'gols', 'assistencias', 'mvp', 'clean_sheet']

    def __init__(self, *args, jogadores_confirmados=None, jogo=None, **kwargs):
        super().__init__(*args, **kwargs)
        if jogadores_confirmados is not None and jogo is not None:
            # Excluir jogadores que já têm um desempenho registrado neste jogo
            desempenhos_registrados = DesempenhoJogador.objects.filter(jogo_dia=jogo).values_list('jogador_id', flat=True)
            self.fields['jogador'].queryset = jogadores_confirmados.exclude(id__in=desempenhos_registrados)
