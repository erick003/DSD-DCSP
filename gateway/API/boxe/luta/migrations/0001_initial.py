# Generated by Django 4.1.6 on 2023-02-07 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Boxeador",
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
                ("nome", models.CharField(max_length=100)),
                ("categoria_de_peso", models.CharField(max_length=100)),
                ("registro", models.CharField(max_length=100)),
                ("postura", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Luta",
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
                ("data", models.DateField()),
                ("local", models.CharField(max_length=100)),
                (
                    "boxeador1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="luta_boxeador1",
                        to="luta.boxeador",
                    ),
                ),
                (
                    "boxeador2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="luta_boxeador2",
                        to="luta.boxeador",
                    ),
                ),
                (
                    "vencedor",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="luta_vencedor",
                        to="luta.boxeador",
                    ),
                ),
            ],
        ),
    ]
