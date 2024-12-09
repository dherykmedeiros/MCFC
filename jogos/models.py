from django.db import models
from usuarios.models import NewUser

# Create your models here.
class Jogo(models.Model):
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
  
class Presenca(models.Model):
  jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE,related_name='presencas')
  usuario = models.ForeignKey(NewUser, on_delete=models.CASCADE,related_name='presencas')
  confirmado = models.BooleanField(default=False)
  data_confirmacao= models.DateTimeField(auto_now_add=True)

  class Meta:
    unique_together = ('usuario', 'jogo')
  
  def __str__(self):
    return f"{self.usuario} - {self.jogo} ({'Confirmado' if self.confirmado else 'Não confirmado'})"