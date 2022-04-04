from ghana_card.models import BaseModel
from django.db import models

class Pharmacy(BaseModel):
    
    name = models.CharField(null=False, blank=False, max_length=50, unique=True)
    description = models.CharField(null=True, blank=True, max_length=300)

    def __str__(self):
        return f'{self.name}'

class Drug(BaseModel):
    
    name = models.CharField(null=False, blank=False, max_length=50, unique=True)
    description = models.CharField(null=True, blank=True, max_length=300)
    price = models.FloatField(null=True, blank=True)
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.PROTECT, related_name='drugs')

    def __str__(self):
        return f'{self.name}'
