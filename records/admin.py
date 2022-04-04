from django.contrib import admin
from .models import Records

@admin.register(Records)
class RecordsAdmin(admin.ModelAdmin):
     list_display = ('name_of_patient', 'patient_id',)
     search_fields = ('name_of_patient', 'patient_id',)


