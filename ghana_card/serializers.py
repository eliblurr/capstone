from rest_framework import serializers
from .models import GhanaCard

class GhanaCardSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GhanaCard
        fields = '__all__'