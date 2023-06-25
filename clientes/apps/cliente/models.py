from django.db import models
from .utils import get_google_maps_client
import uuid
from location_field.models.plain import PlainLocationField

class Cliente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombres = models.CharField('Nombres', max_length=100, blank=True, null=True)
    apellidos = models.CharField('Apellidos', max_length=100, blank=True, null=True)
    email = models.EmailField('E-mail', blank=True, null=True)
    telefono = models.CharField('Teléfono', max_length=20)
    direccion = models.CharField('Dirección', max_length=200, blank=True, null=True)
    fecha_union = models.DateField('Fecha de Unión', null=True, blank=True)
    activo = models.BooleanField(default=True)
    notas = models.TextField(blank=True, null=True)
    location = models.CharField('Ubicacion', max_length=100, blank=True, null=True) 
