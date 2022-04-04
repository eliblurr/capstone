from django.db import models

class BaseModel(models.Model):
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True

class GhanaCard(BaseModel): 

    SEX = (
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other'),
    )
   
    surname = models.CharField(null=False, blank=False, max_length=50)
    first_name = models.CharField(null=False, blank=False, max_length=50)
    nationality = models.CharField(null=False, blank=False, max_length=50)
    other_names = models.CharField(null=True, blank=True, max_length=200)
    place_of_issuance = models.CharField(null=False, blank=False, max_length=200)
    personal_id_number = models.CharField(null=False, blank=False, max_length=50, unique=True) # ghana_card_number
    document_number = models.CharField(null=False, blank=False, max_length=50, unique=True) # tbd
    sex = models.CharField(max_length=6, choices=SEX, null=False, blank=False) 
    date_of_issuance = models.DateTimeField(auto_now_add=True)
    date_of_expiry = models.DateTimeField()
    date_of_birth = models.DateField()
    height = models.FloatField()

    def __str__(self):
        return f'{self.first_name} {self.surname}'