from appointment.models import Appointment
from ghana_card.models import BaseModel
from django.conf import settings
from django.db import models

from pharmacy.models import Drug
from patient.models import Patient
from record.models import Record

class Visit(BaseModel):

    visit_statuses = (
        ('registered','registered'),
        ('screened','screened'),
        ('examined','examined'),
    )
    
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='visits')
    appointment = models.OneToOneField(Appointment, on_delete=models.DO_NOTHING, related_name='visit', null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, related_name='visits')
    records = models.ForeignKey(Record, on_delete=models.DO_NOTHING, related_name='visits')
    end_time = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    date = models.DateField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return f'Dr. {self.doctor.first_name} {self.doctor.last_name}'

class Payment(BaseModel):
    
    amount = models.FloatField(null=False, blank=False)
    bill = models.ForeignKey("Bill", on_delete=models.CASCADE, related_name='payments')
    
    def __str__(self):
        return self.amount

class Bill(BaseModel):

    class Type(models.TextChoices):
        LUMPSUM = 'lump-sum', 'lump-sum'
        INSTALLMENT = 'installment', 'installment'

    class Status(models.TextChoices):
        WAIVED = 'waived', 'waived'
        PENDING = 'pending', 'pending'
        CANCELLED = 'cancelled', 'cancelled'

    total = models.FloatField(null=False, blank=False)
    insurance_coverage = models.FloatField(null=True, blank=True, default=0)
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.PENDING, null=False, blank=False)
    bill_type = models.CharField(max_length=15, choices=Type.choices, null=False, blank=False)
    insurance = models.ForeignKey("Insurance", on_delete=models.PROTECT, related_name='bills')

    def paid(self):
        return sum([payment.amount for payment in self.payments])

    def debit(self):
        return self.total - (self.insurance_coverage+self.paid())

    def make_payment(self, amount):
        if self.debit() > amount:
            raise ValueError('amount exceeds debit')
        if self.bill_type==Type.LUMPSUM and self.debit()!=amount:
            raise ValueError('insufficient credit')
        payment = Payment.objects.create(amount=amount, bill=self)
        return payment

class Insurance(BaseModel):
    
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

# visit = models.OneToOneField("Visit", on_delete=models.PROTECT, related_name='bill')

# class Prescription(BaseModel):

#     class Status(models.TextChoices):
#         OUTOFSTOCK = 'out-of-stock', 'out-of-stock'
#         OUTSOURCE = 'outsourced', 'outsourced'
#         PENDING = 'pending', 'pending'
#         ISSUED = 'issued', 'issued'
    
#     note = models.TextField(null=False, blank=False)
#     drug = models.ForeignKey(Drug, on_delete=models.DO_NOTHING, null=False, blank=False)
#     status = models.CharField(max_length=15, choices=Status.choices, default=Status.PENDING, null=False, blank=False)
#     issued_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='prescriptions')
#     visit = models.OneToOneField('Visit', on_delete=models.CASCADE, related_name='prescription')

#     class Meta:
#         unique_together = ('visit', 'status',)
    