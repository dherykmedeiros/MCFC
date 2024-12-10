from django.db import models
from usuarios.models import NewUser
from jogadores.models import Jogador
import uuid

# Create your models here.
class Jogo(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  titulo = models.CharField(max_length=150)
  local = models.CharField(max_length=150)
  data_jogo = models.DateField()
  hora_jogo = models.TimeField()
  time_casa = models.CharField(max_length=150)
  time_visitante = models.CharField(max_length=150)
  placar_casa = models.IntegerField(blank=True, null=True)
  placar_visitante = models.IntegerField(blank=True, null=True)
  arte_jogo = models.ImageField(blank=True, null=True)

  def __str__(self):
    return f"{self.titulo} - {self.data_jogo}"
  

class DesempenhoJogador(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  jogo_dia = models.ForeignKey(Jogo, on_delete=models.CASCADE, related_name='desempenhos')
  jogador = models.ForeignKey(Jogador, on_delete=models.CASCADE, related_name='desempenhos')
  jogo = models.IntegerField(default=0)
  gols = models.IntegerField(default=0)
  assistencias = models.IntegerField(default=0)
  mvp = models.BooleanField(default=False)
  clean_sheet = models.BooleanField(default=False)

  class Meta:
    unique_together = ('jogo_dia', 'jogador')

  def __str__(self):
    return f"{self.jogador} - {self.jogo_dia}"

  
class Presenca(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE,related_name='presencas')
  usuario = models.ForeignKey(NewUser, on_delete=models.CASCADE,related_name='presencas')
  confirmado = models.BooleanField(default=False)
  data_confirmacao= models.DateTimeField(auto_now_add=True)

  class Meta:
    constraints = [
      models.UniqueConstraint(fields=['usuario', 'jogo'], name='unique_usuario_jogo')
    ]

  def __str__(self):
    return f"{self.usuario} - {self.jogo} ({'Confirmado' if self.confirmado else 'Não confirmado'})"