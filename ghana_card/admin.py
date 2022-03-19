from django.contrib import admin
from .models import GhanaCard

@admin.register(GhanaCard)
class GhanaCardAdmin(admin.ModelAdmin):
    list_filter = ('sex','nationality',)
    list_display = ('first_name', 'surname', 'other_names', 'document_number', 'personal_id_number')
    search_fields = ('other_names','first_name','surname', 'document_number', 'personal_id_number',)
