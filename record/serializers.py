from .models import Record, Prescription, RecordRequest, Vitals
from patient.serializers import PatientSerializer
from django.contrib.auth import get_user_model
from users.serializers import UserSerializer
from rest_framework import serializers

User = get_user_model()

class PrescriptionSerializer(serializers.ModelSerializer):

    visit = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    issued_by = serializers.PrimaryKeyRelatedField(many=False, queryset=User.objects.filter(role=User.Types.PHARMACIST).all(), required=True)

    class Meta:
        model = Prescription
        fields = '__all__'

class RecordSerializer(serializers.ModelSerializer):
    doctor = serializers.PrimaryKeyRelatedField(many=False, queryset=User.objects.filter(role=User.Types.DOCTOR).all(), required=True)
    
    class Meta:
        model = Record
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['doctor'] = UserSerializer(many=False)
        self.fields['patient'] = PatientSerializer(many=False)
        self.fields['prescriptions'] = PrescriptionSerializer(many=False)
        return super(RecordSerializer, self).to_representation(instance)

class RecordRequestSerializer(serializers.ModelSerializer):

    status = serializers.CharField(read_only=True)

    class Meta:
        model = RecordRequest
        fields = '__all__'

class VitalsSerializer(serializers.ModelSerializer):


    class Meta:
        model = Vitals
        fields = '__all__'