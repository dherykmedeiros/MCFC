# Generated by Django 5.1.4 on 2024-12-09 14:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('local', models.CharField(max_length=150)),
                ('data_jogo', models.DateField()),
                ('hora_jogo', models.TimeField()),
                ('time_casa', models.CharField(max_length=150)),
                ('time_visitante', models.CharField(max_length=150)),
                ('placar_casa', models.IntegerField(blank=True, null=True)),
                ('placar_visitante', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Presenca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmado', models.BooleanField(default=False)),
                ('data_confirmacao', models.DateTimeField(auto_now_add=True)),
                ('jogo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='presencas', to='jogos.jogo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='presencas', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('usuario', 'jogo')},
            },
        ),
    ]