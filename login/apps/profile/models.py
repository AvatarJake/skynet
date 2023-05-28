
from django.conf import settings
User = settings.AUTH_USER_MODEL

from djoser.signals import user_registered

from django.db import models

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')

    fotografia = models.ImageField(default='media/users/user_default_profile.png', upload_to='media/users/pictures',blank=True,null=True,verbose_name='Fotografia')
    telefono = models.CharField(max_length=20,blank=True,null=True,verbose_name='Telefono')
    fecha_contratacion = models.DateField(blank=True,null=True,verbose_name='Fecha de Contratacion')
    direccion = models.CharField(max_length=200,blank=True,null=True,verbose_name='Direccion')
    fecha_nacimiento = models.DateField(blank=True,null=True,verbose_name='Fecha de Nacimiento')
    numero_identificacion = models.CharField(max_length=25, unique=True)
    ubicacion=models.CharField(max_length=50,null=True,blank=True)
    informacion = models.TextField(max_length=200, null=True, blank=True)

def post_user_registered(request, user, *args, **kwargs):
        user=user
        Profile.objects.create(user.user)

user_registered.connect(post_user_registered)