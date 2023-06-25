# Generated by Django 3.2.16 on 2023-06-07 04:20

from django.db import migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0005_cliente_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='name',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='location',
            field=location_field.models.plain.PlainLocationField(default='14.80081660623604, -89.54580370192767', max_length=63, null=True),
        ),
    ]
