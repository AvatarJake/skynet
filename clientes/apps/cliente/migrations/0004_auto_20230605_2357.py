# Generated by Django 3.2.16 on 2023-06-06 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_auto_20230605_2345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='ubicacion',
        ),
        migrations.AddField(
            model_name='cliente',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='UbicacionCliente',
        ),
    ]