from rest_framework import serializers
from .models import Patient, Allergy

class PatientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Patient
        fields = '__all__'

class AllergySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Allergy
        fields = '__all__'
