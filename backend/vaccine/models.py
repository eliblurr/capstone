from django.core.validators import MaxValueValidator, MinValueValidator
from ghana_card.models import BaseModel
from django.db import models

class Vaccine(BaseModel):
    
    name = models.CharField(null=False, blank=False, max_length=50)
    description = models.CharField(null=True, blank=True, max_length=300)

    recommended_dosage = models.IntegerField(null=False, blank=False, default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])

    def __str__(self):
        return f'{self.name}'

'''
-> patient vaccine
patient
vaccine
administered_by -> ofType[nurse]
dosage
date of issuance
next dosage due 
injection site [arm[left/right upper arm], legs, thighs, buttocks, head, chest, eyes]
location[place, district, sub-district, community, town/village, region]
'''