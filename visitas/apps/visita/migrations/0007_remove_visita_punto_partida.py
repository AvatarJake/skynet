# Generated by Django 3.2.16 on 2023-06-25 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visita', '0006_visita_direccion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visita',
            name='punto_partida',
        ),
    ]