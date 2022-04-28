from .models import Insurance, Bill, Payment, Visit#, Prescription
from patient.serializers import PatientSerializer
from django.contrib.auth import get_user_model
from users.serializers import UserSerializer
from rest_framework import serializers

User = get_user_model()

class InsuranceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Insurance
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Payment
        fields = '__all__'

class BillSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bill
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['payments'] = PaymentSerializer(many=True)
        self.fields['insurance'] = InsuranceSerializer(many=False)
        return super(BillSerializer, self).to_representation(instance)

# class PrescriptionSerializer(serializers.ModelSerializer):

#     visit = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
#     issued_by = serializers.PrimaryKeyRelatedField(many=False, queryset=User.objects.filter(role=User.Types.PHARMACIST).all(), required=True)

#     class Meta:
#         model = Prescription
#         fields = '__all__'

class VisitSerializer(serializers.ModelSerializer):
    doctor = serializers.PrimaryKeyRelatedField(many=False, queryset=User.objects.filter(role=User.Types.DOCTOR).all(), required=True)

    class Meta:
        model = Visit
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['bill'] = BillSerializer(many=False, required=False)
        self.fields['doctor'] = UserSerializer(many=False)
        self.fields['patient'] = PatientSerializer(many=False)
        # self.fields['prescription'] = PrescriptionSerializer(many=False)
        return super(VisitSerializer, self).to_representation(instance)