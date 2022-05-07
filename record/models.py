from django.core.exceptions import ValidationError
from multiselectfield import MultiSelectField
from ghana_card.models import BaseModel
from django.conf import settings
from django.db import models

from pharmacy.models import Drug
from patient.models import Patient
from django.core.validators import RegexValidator


class Record(BaseModel): 

    class ENQUIRY_TYPE(models.TextChoices):
        GENERAL = 'general', 'general'
        RESPIRATORY = 'respiratory-system', 'respiratory-system'
        CARDIOVASCULAR = 'cardiovascular-system', 'cardiovascular-system'
        GYNAECOLOGICAL = 'gynaecological-system', 'gynaecological-system'
        MUSCULOSCKELETAL = 'musculoskeletal-system', 'musculoskeletal-system'
        CNS = 'central-nervous-system', 'central-nervous-system'
        UROGENITAL = 'urogenital', 'urogenital'
        PSYCHIATRIC = 'psychiatric', 'psychiatric'
    
    DIAGNOSIS_TYPE = (
        ('from-patient-diagnosis-history', 'from-patient-diagnosis-history'),
        ('from-doctor-diagnosis-history', 'from-doctor-diagnosis-history'),
    )

    EXAMINATION_FINDINGS_TYPE = (
        ('General findings', 'General findings'),
        ('Cardiovascular system', 'Cardiovascular system'),
        ('Respiratory system', 'Respiratory system'),
        ('Abdominal', 'Abdominal'),
        ('Central Nervous system', 'Central Nervous system'),
        ('Examination of abdomen', 'Examination of abdomen'),
        ('Pelvic/Vaginal Examination', 'Pelvic/Vaginal Examination'),
        ('Speculum Examination', 'Speculum Examination'),
        ('Musculoskeletal system', 'Musculoskeletal system'),
        ('Other findings', 'Other findings'),
    )

    INVESTIGATION_REQUEST = (
        ('laboratory', 'laboratory'),
        ('radiology', 'radiology'),
        ('ECG', 'ECG'),
        ('others', 'others'),
        ('endoscopy', 'endoscopy'),
        ('histopathology', 'histopathology'),
        ('from-patient-diagnosis-history', 'from-patient-diagnosis-history'),
        ('from-doctor-diagnosis-history', 'from-doctor-diagnosis-history'),
        ('audiology', 'audiology'),
    )

    date = models.DateField(auto_now_add=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='records')
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='records')
    diagnosis_type = models.CharField(max_length=100, choices=DIAGNOSIS_TYPE, null=False, blank=False)
    record_type = models.CharField(max_length=100, choices=ENQUIRY_TYPE.choices, null=False, blank=False)
    patient_complaint = models.CharField(null=False, blank=False, max_length=1000)
    management_plan = models.CharField(null=False, blank=False, max_length=1000)
    diagnosis = models.CharField(null=False, blank=False, max_length=1000)
    notes = models.CharField(null=False, blank=False, max_length=1000)

    examination_finding_types = MultiSelectField(choices=EXAMINATION_FINDINGS_TYPE, max_choices=10,)
    investigation_request = MultiSelectField(choices=INVESTIGATION_REQUEST, max_choices=9,)

    # history invferred form patient past records

    def __str__(self):
        return f'{self.patient.first_name} {self.patient.last_name}'

class Vitals(BaseModel):

    date = models.DateField(auto_now_add=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='vitals')
    weight = models.CharField(null=False, blank=False, max_length=10)
    height = models.CharField(null=False, blank=False, max_length=10)
    temperature = models.CharField(null=False, blank=False, max_length=10)
    blood_pressure = models.CharField(null=False, blank=False, max_length=10)
    SpO2 = models.FloatField(null=False, blank=False, max_length=10)
    BpM = models.CharField(null=False, blank=False, max_length=10)
    notes = models.CharField(null=False, blank=False, max_length=1000)
    record = models.ForeignKey(Record, on_delete=models.CASCADE, related_name='vitals')  

    def __str__(self):
        return f'{self.patient.first_name} {self.patient.last_name}'

class Prescription(BaseModel):

    class Status(models.TextChoices):
        OUTOFSTOCK = 'out-of-stock', 'out-of-stock'
        OUTSOURCE = 'outsourced', 'outsourced'
        PENDING = 'pending', 'pending'
        ISSUED = 'issued', 'issued'
    
    note = models.TextField(null=False, blank=False)
    drug = models.ForeignKey(Drug, on_delete=models.DO_NOTHING, null=False, blank=False)
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.PENDING, null=False, blank=False)
    issued_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='prescriptions')
    extra_prescriptions = models.CharField(null=False, blank=False, max_length=1000)
    record = models.OneToOneField(Record, on_delete=models.CASCADE, related_name='prescriptions')

    class Meta:
        unique_together = ('record', 'status',)
        constraints = [
            models.CheckConstraint(
                check=models.Q(drug__isnull=False) | models.Q(extra_prescriptions__isnull=False),
                name='not_both_null'
            )
        ]

PHONE = r'^\+1?\d{9,15}$'    
EMAIL = r'^[\w\-\.]+@([\w\-]+\.)+[\w\-]{2,4}$'

class RecordRequest(BaseModel):
    
    class Status(models.TextChoices):
        DECLINED = 'declined', 'declined'
        ACCEPTED = 'accepted', 'accepted'
        PENDING = 'pending', 'pending'

    class RECORDTYPE(models.TextChoices):
        VISIT = 'visit', 'visit'
        LAB = 'lab', 'lab'
        PENDING = 'pending', 'pending'

    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.CharField(max_length=50, null=True, blank=True, validators=[
            RegexValidator(
                regex=EMAIL,
                message='invalid email format',
            ),
        ]
    )
    phone = models.CharField(max_length=50, null=True, blank=True, validators=[
            RegexValidator(
                regex=PHONE,
                message='invalid phone format',
            ),
        ]
    )
    subdomain_id = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.PENDING, null=False, blank=False)
    record_type = models.CharField(max_length=15, choices=RECORDTYPE.choices, null=False, blank=False)
    ghana_card_no = models.CharField(max_length=100, null=False, blank=False)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
