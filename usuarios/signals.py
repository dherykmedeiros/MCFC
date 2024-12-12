from django.db.models.signals import post_save
from django.dispatch import receiver
from jogadores.models import Jogador
from usuarios.models import NewUser


@receiver(post_save, sender=NewUser)
def criar_jogador(sender, instance, created, **kwargs):
    if created:
        Jogador.objects.create(jogador=instance)
