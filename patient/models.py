from ghana_card.models import BaseModel
from django.db import models

class Patient(BaseModel): 

    SEX = (
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other'),
    )
   
    last_name = models.CharField(null=False, blank=False, max_length=50)
    first_name = models.CharField(null=False, blank=False, max_length=50)
    nationality = models.CharField(null=False, blank=False, max_length=50)
    other_names = models.CharField(null=True, blank=True, max_length=200)
    ghana_card_number = models.CharField(null=True, blank=True, max_length=50, unique=True)
    sex = models.CharField(max_length=6, choices=SEX, null=False, blank=False) 
    date_of_birth = models.DateField()
    height = models.FloatField()
   
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
