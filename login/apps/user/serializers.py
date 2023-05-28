from djoser.serializers import UserCreateSerializer

from django.contrib.auth import get_user_model
User=get_user_model()

class UserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = [
            'id',
            'stripe_customer_id',
            'stripe_account_id',
            'email',
            'username',
            'slug',
            'first_name',
            'last_name',
            'agreed',
            'is_active',
            'is_staff',
            'role',
            'vefified',
        ]

class UserListSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model= User
        fields = [
            'id',
            'stripe_customer_id',
            'stripe_account_id',
            'stripe_payment_id',
            'email',
            'username',
            'verified',
        ]