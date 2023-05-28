
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import MaxValueValidator, MinValueValidator
from slugify import slugify

from django.db.models.signals import post_save
import requests
from django.conf import settings
activecapaingn_url = settings.ACTIVE_CAMPAIGN_URL
activecapaingn_KEY = settings.ACTIVE_CAMPAIGN_KEY
from djoser.signals import user_registered
import uuid,json
# import stripe
# stripe.api_key = settings.STRIPE_SECRET_KEY
import requests 
from core.producer import producer
import re

pattern_special_characters = r'badmin\b|[!"@#$%&¬()_\-+\=[{¨,;:<>/*~]¡?¿}\s]'

def user_profile_directory_path(instance,filename):
    profile_pic_name = 'users/{0}/profile.jpg'.format(str(uuid.uuid4()))

def user_banner_directory_path(instance,filename):
    banner_pic_name = 'users/{0}/banner.jpg'.format(str(uuid.uuid4()))

class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):    
        
        def create_slug(username):
            if re.search(pattern_special_characters, username):
                raise ValueError('El usuario contiene caracteres invalidos')
            username =re.sub(pattern_special_characters, '', username)
            return slugify(username)
        
        if not email:
            raise ValueError('El usuario debe tener un correo electronico')
        
        email = self.normalize_email(email)   
        extra_fields['slug']= create_slug(extra_fields['username'])
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
        
        item={}
        item['id']=str(user.id)
        item['email']=user.Email
        item['username']=user.username
        producer.produce(
            'login',
            key='create_user',
            value=json.dumps(item).encode('utf-8')
        )
        producer.flush()
        return user

    def create_superuser(self,email,password,**extra_fields):
        user=self.create_user(email,password,**extra_fields)
        user.is_superuser = True
        user.is_staff=True
        user.role="admin"
        user.verified=True
        user.become_seller=True
        user.save(using=self._db)

        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    roles= (
        ('administrador', 'Administrador'),
        ('supervisor', 'Supervisor'), 
        ('tecnico', 'Tecnico'), 
        
    )

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    stripe_customer_id=models.CharField(max_length=100, blank=True, null=True)
    stripe_account_id=models.CharField(max_length=100, blank=True, null=True)
    stripe_payment_id=models.CharField(max_length=100, blank=True, null=True)

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    slug=models.CharField(max_length=100, unique=True, blank=True)

    first_name = models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)
    is_online = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    role = models.CharField(max_length=100,choices=roles, default='Tecnico')
    verified = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    def save(self, *args, **kwargs):
        self.slug =slugify((self.username))
        counter = 1
        while UserAccount.objects.filter(slug=self.slug).exists():
            self.slug=f"{self.slug}-{counter}"
            counter += 1
        super().save(*args, **kwargs)

        def __str__(self):
            return self.email
    
    # # def post_user_confirmed(request, user, *args, **kwargs):

    # #     #esto define el usuario
    # #     user=user
    # #     # creando cliente en stripe
    # #     stripe_customer = stripe.Customer.create(
    # #         email=user.email,
    # #         name=user.first_name+" "+user.last_name
    # #     )
    # #     user.stripe_customer.id = stripe_customer["id"]
    # #     user.save()

    # #     connect_account = stripe.Account.create(
    # #         type = "express",
    # #         capabilities = {"card_payments": {"requested":True}, "transfers": {"requested":True}},
    # #     )
    # #     user.stripe_account.id =connect_account["id"]
    # #     user.save()

    # user_registered.connect(post_user_confirmed)

# Create your models here.
