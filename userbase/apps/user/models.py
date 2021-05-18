from django.db import models
from . import UserStatus


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default=UserStatus.REGISTERED)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
