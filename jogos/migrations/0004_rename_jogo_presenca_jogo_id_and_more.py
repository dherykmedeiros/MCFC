# Generated by Django 5.1.4 on 2024-12-09 20:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jogos', '0003_alter_jogo_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='presenca',
            old_name='jogo',
            new_name='jogo_id',
        ),
        migrations.AlterUniqueTogether(
            name='presenca',
            unique_together={('usuario', 'jogo_id')},
        ),
    ]