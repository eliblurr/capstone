from ghana_card.models import BaseModel
from django.conf import settings
from django.db import models

class Break(models.Model):
    start_time = models.TimeField(null=False, blank=False)
    end_time = models.TimeField(null=False, blank=False)

class Schedule(BaseModel):

    DAYS = (
        ('monday', 'monday'),
        ('tuesday', 'tuesday'),
        ('wednesday', 'wednesday'),
        ('thursday', 'thursday'),
        ('friday', 'friday'),
        ('saturday', 'saturday'),
        ('sunday', 'sunday'),
    )
    
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='schedule', on_delete=models.CASCADE)
    day = models.CharField(null=False, blank=False, max_length=50, choices=DAYS)
    start_time = models.TimeField(null=False, blank=False)
    end_time = models.TimeField(null=False, blank=False)
    breaks = models.ManyToManyField(Break)

    def __str__(self):
        return f'{self.doctor}'

    class Meta:
        unique_together = ['day', 'doctor',]



