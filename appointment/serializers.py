from django.contrib.auth import get_user_model
from users.serializers import UserSerializer
from rest_framework import serializers
from .models import Appointment

User = get_user_model()

class AppointmentSerializer(serializers.ModelSerializer):
    doctor = serializers.PrimaryKeyRelatedField(many=False, queryset=User.objects.filter(role=User.Types.DOCTOR).all(), required=True)
    # add patient serializers.PrimaryKeyRelatedFiel here 

    class Meta:
        model = Appointment
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['doctor'] = UserSerializer(many=False)
        # serialize patient here 
        return super(AppointmentSerializer, self).to_representation(instance)

        