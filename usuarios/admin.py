from django.contrib import admin
from .models import NewUser
from jogadores.models import Jogador
from jogos.models import Jogo,Presenca

# Register your models here.

admin.site.register(NewUser)
admin.site.register(Jogador)
admin.site.register(Jogo)

