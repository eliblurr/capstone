from .models import Specialisation
from django.contrib import admin

@admin.register(Specialisation)
class SpecialisationAdmin(admin.ModelAdmin):
   
    list_display = ('name', 'description',)
    search_fields = ('name','description',)
