from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    name = models.CharField(max_length=50, default="anonymous")
    email = models.CharField(max_length=50, unique=True)

    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    phone = models.CharField(max_length=13, blank=True, null=True)

    session_token = models.CharField(max_length=10, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
