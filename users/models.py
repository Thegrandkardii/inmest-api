from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authentication.models import Token

# Create your models here.

class IMUser(AbstractUser):
    USER_TYPES = [
        ('EIT', 'EIT'),
        ('TEACHING_FELLOW', 'Teaching Fellow'),
        ('ADMIN_STAFF', 'Admin Staff'),
        ('ADMIN', 'Admin'),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    date_created = models.DateTimeField(auto_now_add=True)  

class Cohort(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    year = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE)
    

     