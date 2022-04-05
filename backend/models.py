from django.db import models

class BaseModel(models.Model):
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Records(BaseModel): 

#take away the (name of patient) field
#make the patient id a foreign key relation to patient model
#make sex constant CAPS
#create sex char field for sex choices
#make doctor foreign key to the doctor model

    name_of_patient = models.CharField(null=False, blank=False, max_length=200)
    patient_id = models.CharField(null=False, blank=False, max_length=200, unique=True)
    Date_of_arrival = models.DateTimeField(auto_now_add=True)
    Sex = (
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other'),
    )
    Doctor_in_charge = models.CharField(null=False, blank=False, max_length=200)
    Patient_complaint = models.CharField(null=False, blank=False, max_length=200)
    history_of_complaints = models.CharField(null=False, blank=False, max_length=200)
    on_direct_questionining = models.CharField(null=False, blank=False, max_length=200)
    system_enquiring = (
        ('General', 'General'),
        ('Respiratory system', 'Respiratory system'),
        ('Cardiovascular system', 'Cardiovascular system'),
        ('Urogenital system', 'Urogenital system'),
        ('Gynaecological system', 'Gynaecological system'),
        ('Central Nervous System', 'Central Nervous System'),
        ('Musculoskeletal system', 'Musculoskeletal system'),
        ('Psychiatric', 'Psychiatric'),
    )
    Patient_History = (
        ('Past Medical History', 'Past Medical History'),
        ('Drug History', 'Drug History'),
        ('Allergies', 'Allergies'),
        ('Obs and Gynae History', 'Obs and Gynae History'),
        ('Family History', 'Family History'),
        ('Social History', 'Social Hisory'),
        ('other', 'other'),
    )
    Examination_findings = (
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
    Diagnosis = (
        ('From Patient Diagnosis History', 'From Patient Diagnosis History'),
        ('From Doctor Diagnosis History', 'From Doctor Diagnosis History'),
    )
    Investigation_Request = (
        ('Laboratory', 'Laboratory'),
        ('Radiology', 'Radiology'),
        ('ECG', 'ECG'),
        ('Others', 'Others'),
        ('Endoscopy', 'Endoscopy'),
        ('Histopathology', 'Histopathology'),
        ('From Patient Investigation History', 'From Patient Investigation History'),
        ('From Doctor Request History', 'From Doctor Request History'),
        ('Audiology', 'Audiology'),
    )
    management_plan = models.CharField(null=False, blank=False, max_length=200)
    drug_prescription = models.CharField(null=False, blank=False, max_length=200)


    def __str__(self):
        return f'{self.name}'

