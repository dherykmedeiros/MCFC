# Generated by Django 5.1.4 on 2024-12-10 13:10

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jogos', '0006_alter_presenca_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presenca',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]