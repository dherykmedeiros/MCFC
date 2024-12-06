from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class NewUser(AbstractUser):
  email = models.EmailField(max_length=255, unique=True,blank=True,null=True)
  posicoes = (
    ('GK', 'goleiro'),
    ('ZG', 'zagueiro'),
    ('LD', 'lateral direito'),
    ('LE', 'lateral esquerdo'),
    ('VOL', 'volante'),
    ('MEI', 'meio-campista'),
    ('AT', 'atacante')
  )
  posicao = models.CharField(max_length=3, choices=posicoes,blank=False,null=False)
  descricao = models.TextField(blank=True,null=True)

  def __str__(self):
    return self.username
