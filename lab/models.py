from datetime import date
from enum import unique
from ghana_card.models import BaseModel
from django.conf import settings
from visit.models import Visit
from django.db import models

class TestType(BaseModel):
    
    name = models.CharField(null=False, blank=False, max_length=50, unique=True)
    description = models.CharField(null=True, blank=True, max_length=300)


    def __str__(self):
        return f'{self.name}'

class LabTest(BaseModel):    
    
    test_type = models.ForeignKey('TestType', related_name='labs', on_delete=models.CASCADE)
    lab_technician = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='labs', on_delete=models.CASCADE)
    visit = models.ForeignKey(Visit, related_name='labs', on_delete=models.CASCADE)
    name_of_lab_technician = models.CharField(null=False, blank=False, max_length=200)
    name_of_doctor = models.CharField(null=False, blank=False, max_length=200)
    name_of_patient = models.CharField(null=False, blank=False, max_length=200)
    dosage = models.CharField(null=False, blank=False, max_length=50)
    blood_level = models.CharField(null=False, blank=False, max_length=50, unique = True)
    urine_test = models.CharField(null=False, blank=False, max_length=50, unique=True)
    cerebrospinal_fluid_test = models.CharField(null=False, blank=False, max_length=50, unique=True)
    synovial_fluid_test = models.CharField(null=False, blank=False, max_length=50, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    # record

    def __str__(self):
        return f'{self.test_type.name}'
