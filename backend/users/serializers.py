from specialisation.serializers import SpecialisationSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import ValidationError
from pharmacy.serializers import PharmacySerializer
from specialisation.models import Specialisation
from .models import User, Doctor, Pharmacist
from django.contrib.auth import authenticate
from rest_framework import serializers
from pharmacy.models import Pharmacy
from django.db import transaction

class DoctorSerializer(serializers.ModelSerializer):
    specialisation = serializers.PrimaryKeyRelatedField(many=False, queryset=Specialisation.objects.all(), required=True)

    class Meta:
        model = Doctor
        fields = ['specialisation']

    def to_representation(self, instance):
        self.fields['specialisation'] = SpecialisationSerializer(many=False)
        return super(DoctorSerializer, self).to_representation(instance)

class PharmacistSerializer(serializers.ModelSerializer):
    pharmacy = serializers.PrimaryKeyRelatedField(many=False, queryset=Pharmacy.objects.all(), required=True)

    class Meta:
        model = Pharmacist
        fields = ['pharmacy']

    def to_representation(self, instance):
        self.fields['pharmacy'] = PharmacySerializer(many=False)
        return super(PharmacistSerializer, self).to_representation(instance)

class UserSerializer(serializers.ModelSerializer):

    doctor = DoctorSerializer(many=False, required=False)
    pharmacist = PharmacistSerializer(many=False, required=False)

    class Meta:
        model = User
        fields = ['email','first_name','last_name','phone','employee_id','other_names','role','id','password', 'doctor', 'pharmacist']
        extra_kwargs = {'password': {'write_only': True}}

    def to_representation(self, instance):
        doctor = self.fields.pop('doctor', None)
        pharmacist = self.fields.pop('pharmacist', None)

        profile = doctor if instance.role==User.Types.DOCTOR else pharmacist if instance.role=='pharmacist' else None

        if profile:self.fields.update({'profile':profile})
        return super(UserSerializer, self).to_representation(instance)

    @transaction.atomic
    def create(self, validated_data):
        doctor = validated_data.pop('doctor', None)
        pharmacist = validated_data.pop('pharmacist', None)

        if validated_data['role']==User.Types.DOCTOR and not doctor:
            raise ValidationError(detail='profile with key doctor required', code=422)

        if validated_data['role']==User.Types.PHARMACIST and not pharmacist:
            raise ValidationError(detail='profile with key pharmacist required', code=422)
            
        user = User.objects.create_user(**validated_data)
        
        if user.role=='doctor':
            Doctor.objects.create(user=user, **doctor)

        if user.role=='pharmacist':
            Pharmacist.objects.create(user=user, **pharmacist)
        
        return user

    @transaction.atomic
    def update(self, instance, validated_data):
        doctor = validated_data.pop('doctor', None)
        pharmacist = validated_data.pop('pharmacist', None)
        password = validated_data.pop('password', None)

        if password:
            instance.set_password(password)

        [setattr(instance, k, v) for k, v in validated_data.items()]
        instance.save()
        if instance.role==User.Types.DOCTOR and doctor:
            [setattr(instance.doctor, k, v) for k, v in doctor.items()]
        if instance.role==User.Types.PHARMACIST and pharmacist:
            [setattr(instance.doctor, k, v) for k, v in pharmacist.items()]
        instance.save()

        # if validated_data.get('passwod')
        # print(validated_data)

        return instance

class LogOutSerializer(serializers.Serializer):
    refresh = serializers.CharField(required=True)

# class PasswordSerializer(serializers.Serializer):
#     password = serializers.CharField(required=True)

class LoginSerializer(serializers.Serializer):

    employee_id = serializers.CharField(write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    user = UserSerializer(read_only=True)
   
    def validate(self, data):
        employee_id = data['employee_id']
        password = data['password']
        user = authenticate(employee_id=employee_id, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid login credentials")

        if not user.is_active:
            raise serializers.ValidationError("user account has been deactivated")

        try:
            refresh = RefreshToken.for_user(user)

            return {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': user
            }

        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")

# PasswordResetSerializer
