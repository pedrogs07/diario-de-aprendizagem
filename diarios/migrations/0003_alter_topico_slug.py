# Generated by Django 5.0.2 on 2024-02-11 23:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("diarios", "0002_topico_dono"),
    ]

    operations = [
        migrations.AlterField(
            model_name="topico",
            name="slug",
            field=models.SlugField(default=""),
        ),
    ]
