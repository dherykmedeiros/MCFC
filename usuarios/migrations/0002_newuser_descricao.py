# Generated by Django 5.1.4 on 2024-12-06 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
    ]
