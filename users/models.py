from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from specialisation.models import Specialisation
from pharmacy.models import Pharmacy
from .managers import UserManager
from django.db import models

PHONE = r'^\+1?\d{9,15}$'

class User(AbstractUser):
    username = None

    class Types(models.TextChoices):
        ADMIN = 'admin', 'admin'
        NURSE = 'nurse', 'nurse'
        DOCTOR = 'doctor', 'doctor'
        PHARMACIST = 'pharmacist', 'pharmacist'
        RECEPTIONIST = 'receptionist', 'receptionist'
        LAB_TECHNICIAN = 'lab technician', 'lab technician'
    
    employee_id = models.CharField(max_length=50, unique=True)
    other_names = models.CharField(max_length=150, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True, validators=[
            RegexValidator(
                regex=PHONE,
                message='phone number doesnt comply',
            ),
        ]
    )
    role = models.CharField(max_length=50, choices=Types.choices, null=False, blank=False)

    USERNAME_FIELD = 'employee_id'
    objects = UserManager()

    def __str__(self):
        return f'{self.employee_id}:{self.email}'
  
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='doctor')
    specialisation = models.ForeignKey(Specialisation, on_delete=models.SET_NULL, null=True)
    # schedules = manyToMany

class Pharmacist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='pharmacist')
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.SET_NULL, null=True)
