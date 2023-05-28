from rest_framework import serializers
from .models import profile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=[
            'id',
            'fotografia',
            'ubicacion',
            'informacion',
        ]