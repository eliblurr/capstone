from rest_framework import serializers
from .models import Pharmacy, Drug

class DrugSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Drug
        fields = '__all__'

class PharmacySerializer(serializers.ModelSerializer):
    drugs = DrugSerializer(read_only=True, many=True)
    
    class Meta:
        model = Pharmacy
        fields = '__all__'