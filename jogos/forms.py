from django import forms
from .models import DesempenhoJogador

class DesempenhoJogadorForm(forms.ModelForm):
  class Meta:
    model = DesempenhoJogador
    fields = '__all__'