# Generated by Django 3.2.16 on 2023-06-11 03:33

from django.db import migrations, models
import django.db.models.deletion
import location_field.models.plain
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoServicio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tipo de Servicio')),
            ],
        ),
        migrations.CreateModel(
            name='Visita',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cliente', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cliente')),
                ('fecha_solicitud', models.DateField(blank=True, null=True, verbose_name='Fecha de Solicitud')),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('en proceso', 'En Proceso'), ('operado', 'Operado'), ('cancelado', 'Cancelado')], default='Pendiente', max_length=100)),
                ('fecha_atendido', models.DateField(blank=True, null=True, verbose_name='Fecha de Atendido')),
                ('notas', models.TextField(blank=True, null=True)),
                ('responsable', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tecnico Responsable')),
                ('location', location_field.models.plain.PlainLocationField(default='14.80081660623604, -89.54580370192767', max_length=63, null=True)),
                ('punto_partida', location_field.models.plain.PlainLocationField(default='14.80081660623604, -89.54580370192767', max_length=63, null=True)),
                ('servicio', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='visita.tiposervicio')),
            ],
        ),
    ]
