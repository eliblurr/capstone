from django.contrib import admin
from .models import Vaccine

@admin.register(Vaccine)
class VaccineAdmin(admin.ModelAdmin):
   
    list_filter = ('recommended_dosage',)
    list_display = ('name', 'description', 'recommended_dosage')
    search_fields = ('name','description',)
