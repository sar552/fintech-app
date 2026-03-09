from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    CURRENCY_CHOICES = [
        ('UZS', "O'zbek so'mi"),
        ('USD', 'Dollar'),
        ('EUR', 'Yevro'),
        ('RUB', 'Rubl'),
    ]
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=200, blank= True)
    phone = models.CharField(max_length=20, blank= True)
    default_currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CHOICES,
        default='UZS',
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


