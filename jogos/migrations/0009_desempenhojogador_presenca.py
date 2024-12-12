# Generated by Django 5.1.4 on 2024-12-11 17:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jogos", "0008_desempenhojogador"),
    ]

    operations = [
        migrations.AddField(
            model_name="desempenhojogador",
            name="presenca",
            field=models.ForeignKey(
                default=False,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="desempenhos",
                to="jogos.presenca",
            ),
        ),
    ]
