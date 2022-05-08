from locale import currency
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    
    """Custom User Mdoel"""
    
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"
    
    GENDER_CHOICES = [
        (GENDER_MALE, 'MALE'),
        (GENDER_FEMALE, 'FEMALE'),
        (GENDER_OTHER,'OTHER'),
    ]
    
    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"
    
    LANGUAGE_CHOICES = [
        (LANGUAGE_ENGLISH, 'EN'),
        (LANGUAGE_KOREAN, 'KR'),
    ]
    
    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"
    
    CURRENCY_CHOICES = [
        (CURRENCY_USD, 'USD'),
        (CURRENCY_KRW, 'KRW'),
    ]
    
    avatar = models.ImageField(null=True, blank = True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank = True)
    bio = models.TextField(default="", blank = True)
    birthdate = models.DateField(null=True)
    language = models.CharField(max_length=3, choices=LANGUAGE_CHOICES, null=True, blank = True)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, null=True, blank = True)