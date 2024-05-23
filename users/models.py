from django.contrib.auth.models import AbstractUser
from django.db import models


# User model
class CustomUser(AbstractUser):
    ball = models.IntegerField(default=0)

    def __str__(self):
        return self.username
