from rest_framework import serializers
from .models import *

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields=[
            'id',
            'user_id',
            'nombre',
            'apellidos',
            'email',
            'telefono',
            'direccion', 
            'ubicacion',
            'fecha_union',
            'activo',
            'notas',
        ]