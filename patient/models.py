from ghana_card.models import BaseModel
from django.db import models
from utils import gen_code

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
    code = models.CharField(null=False, blank=False, max_length=50, default=gen_code, unique=True)
    sex = models.CharField(max_length=6, choices=SEX, null=False, blank=False) 
    date_of_birth = models.DateField()
    height = models.FloatField()
   
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Allergy(BaseModel):

    TYPES = (
        ('drug', 'drug'),
        ('food', 'food'),
        ('animal', 'animal'),
        ('contact-dermatitis', 'contact-dermatitis'),
        ('latex', 'latex'),
        ('seasonal', 'seasonal'),
        ('anaphylaxis', 'anaphylaxis'),
        ('mold', 'mold'),
        ('other', 'other'),
    )

    treatment = models.CharField(null=True, blank=True, max_length=1000)
    symptoms = models.CharField(null=False, blank=False, max_length=500)
    substance = models.CharField(null=False, blank=False, max_length=500)
    allergy_type = models.CharField(max_length=50, choices=TYPES, null=False, blank=False) 
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='allergies')
