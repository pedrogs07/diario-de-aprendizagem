# Generated by Django 5.0.2 on 2024-02-10 18:14

import django.db.models.deletion
import hashid_field.field
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Topico",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("topico", models.CharField(max_length=100)),
                ("adicionado_em", models.DateField(auto_now_add=True)),
                ("editado_em", models.DateField(auto_now=True)),
                ("slug", models.SlugField(default="", unique=True)),
            ],
            options={
                "verbose_name": "tópico",
                "verbose_name_plural": "tópicos",
            },
        ),
        migrations.CreateModel(
            name="Entrada",
            fields=[
                (
                    "id",
                    hashid_field.field.HashidAutoField(
                        alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890",
                        min_length=7,
                        prefix="",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("titulo", models.CharField(max_length=100)),
                ("texto", models.TextField()),
                ("adicionada_em", models.DateTimeField(auto_now_add=True)),
                (
                    "topico",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="diarios.topico"
                    ),
                ),
            ],
            options={
                "verbose_name": "entrada",
                "verbose_name_plural": "entradas",
            },
        ),
    ]
