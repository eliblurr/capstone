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

# class EpochSerializer(serializers.Serializer):
#     pass

# {'2022-03-18 00:00:00': [], '2022-03-19 00:00:00': [{'doctor': <User: doctor2:>, 'epochs': [{'start': '04:30:00', 'end': '05:15:00'}, {'start': '05:15:00', 'end': '06:00:00'}]}]}
        