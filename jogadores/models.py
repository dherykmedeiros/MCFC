from django.db import models
from usuarios.models import NewUser
import uuid

# Create your models here.

class Jogador(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  jogador = models.OneToOneField(NewUser, on_delete=models.CASCADE)
  jogos = models.IntegerField(blank=True, null=True, default=None)
  gols = models.IntegerField(blank=True, null=True, default=None)
  assistencias = models.IntegerField(blank=True, null=True,default=None )
  clean_sheet = models.IntegerField(blank=True, null=True, default=None)
  mvp = models.IntegerField(blank=True, null=True, default=None)
  


  def __str__(self):
    return self.jogador.first_name