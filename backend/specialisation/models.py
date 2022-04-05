from ghana_card.models import BaseModel
from django.db import models

class Specialisation(BaseModel):
    
    name = models.CharField(null=False, blank=False, max_length=300, unique=True)
    description = models.CharField(null=True, blank=True, max_length=300)

    def __str__(self):
        return f'{self.name}'
