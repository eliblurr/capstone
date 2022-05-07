from django.contrib.auth import get_user_model
from users.serializers import UserSerializer
from rest_framework import serializers
from .models import LabTest, TestType

User = get_user_model()

class TestTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TestType
        fields = '__all__'

class LabTestSerializer(serializers.ModelSerializer):
    lab_technician = serializers.PrimaryKeyRelatedField(many=False, queryset=User.objects.filter(role=User.Types.LAB_TECHNICIAN).all(), required=True)
    # record = serializers.CharField()

    class Meta:
        model = LabTest
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['lab_technician'] = UserSerializer(many=False)
        self.fields['test_type'] = TestTypeSerializer(many=False)
        return super(LabTestSerializer, self).to_representation(instance)

        