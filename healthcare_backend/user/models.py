from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, unique=True,default='0000000000')


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  
    
    def __str__(self):
        return self.email
