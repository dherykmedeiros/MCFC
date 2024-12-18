# Generated by Django 5.1.4 on 2024-12-10 16:54

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usuarios", "0006_alter_newuser_foto_perfil"),
    ]

    operations = [
        migrations.CreateModel(
            name="Invitation",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "token",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("used", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
