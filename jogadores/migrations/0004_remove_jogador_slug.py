# Generated by Django 5.1.4 on 2024-12-09 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jogadores', '0003_jogador_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jogador',
            name='slug',
        ),
    ]