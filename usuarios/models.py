from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class NewUser(AbstractUser):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
  foto_perfil = models.ImageField(upload_to='fotos/',blank=True, null=True, default=None)

  def __str__(self):
    return self.username
