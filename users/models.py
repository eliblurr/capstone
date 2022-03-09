from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = None

    employee_id = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    other_names = models.CharField(max_length=150)
    surname = models.CharField(max_length=50)

    USERNAME_FIELD = 'employee_id'

    def __str__(self):
        return self.email
