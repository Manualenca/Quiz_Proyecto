from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    is_jugador = models.BooleanField(default=False)
    is_editor = models.BooleanField(default=False)
   
    def __str__(self):
        return self.username