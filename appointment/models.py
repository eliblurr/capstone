from django.core.validators import RegexValidator
from ghana_card.models import BaseModel
from django.conf import settings
from django.db import models

PHONE, MESSAGE = r'^\+?1?\d{9,15}$', "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."

class Appointment(BaseModel):
    
    STATUS =(
        ('pending','pending'),  
        ('booked','booked'),
        ('confirmed','confirmed'),
        ('cancelled','cancelled'),
        ('rescheduled','rescheduled'),
        ('honoured','honoured'),
    )
    
    date = models.DateField(auto_now=False, auto_now_add=False)
    name = models.CharField(max_length=100, null=False, blank=True)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    status = models.CharField(choices=STATUS, default='pending', max_length=15)
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='appointements')
    phone = models.CharField(validators=[RegexValidator(regex=PHONE, message=MESSAGE)], max_length=17, null=True, blank=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f'{self.doctor} -> {self.name} {self.start_time}-{self.end_time}'
