from ghana_card.models import BaseModel
from django.conf import settings
from django.db import models

class Break(models.Model):
    start_time = models.TimeField(null=False, blank=False)
    end_time = models.TimeField(null=False, blank=False)

     # verify 24h format for start and end any make sure end > start

    class Meta:
        unique_together = ('start_time', 'end_time',)

class Schedule(BaseModel):

    DAYS = (
        (0, 'monday'),
        (1, 'tuesday'),
        (2, 'wednesday'),
        (3, 'thursday'),
        (4, 'friday'),
        (5, 'saturday'),
        (6, 'sunday'),
    )
    
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='schedule', on_delete=models.CASCADE)
    day = models.CharField(null=False, blank=False, max_length=50, choices=DAYS)
    start_time = models.TimeField(null=False, blank=False)
    end_time = models.TimeField(null=False, blank=False)
    breaks = models.ManyToManyField(Break)

     # verify 24h format for start and end any make sure end > start

    def __str__(self):
        return f'{self.doctor}'

    class Meta:
        unique_together = ['day', 'doctor',]



