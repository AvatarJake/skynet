# Generated by Django 3.2.16 on 2023-05-24 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fotografia', models.ImageField(blank=True, default='users/user_default_profile.png', null=True, upload_to='media/users/pictures')),
                ('ubicacion', models.CharField(blank=True, max_length=50, null=True)),
                ('informacion', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
