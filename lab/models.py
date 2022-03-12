from ghana_card.models import BaseModel
from django.conf import settings
from django.db import models

class TestType(BaseModel):
    
    name = models.CharField(null=False, blank=False, max_length=50, unique=True)
    description = models.CharField(null=True, blank=True, max_length=300)

    def __str__(self):
        return f'{self.name}'

class LabTest(BaseModel):
    
    test_type = models.ForeignKey('TestType', related_name='tests', on_delete=models.CASCADE)
    lab_technician = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tests', on_delete=models.CASCADE)
    # visit = 1

    def __str__(self):
        return f'{self.test_type.name}'