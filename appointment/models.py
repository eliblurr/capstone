from ghana_card.models import BaseModel
from django.conf import settings
from django.db import models

class Appointment(BaseModel):
    
    STATUS =(
        ('pending','pending'),  
        ('booked','booked'),
        ('confirmed','confirmed'),
        ('cancelled','cancelled'),
        ('rescheduled','rescheduled'),
        ('honoured','honoured'),
    )

    # add patient foreign key
    # patient = models.ForeignKey('Patient', verbose_name=_('Patient'), on_delete=models.DO_NOTHING,related_name='appointments')
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='appointements')

    date = models.DateField(auto_now=False, auto_now_add=False)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    status = models.CharField(choices=STATUS, default='pending', max_length=15)

    class Meta:
        ordering = ['created']

    def __str__(self):
        # replace second .doctor with .patient
        return f'{self.doctor} {self.doctor}'
