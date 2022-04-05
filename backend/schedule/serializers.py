from django.contrib.auth import get_user_model
from users.serializers import UserSerializer
from rest_framework import serializers
from .models import Schedule, Break

User = get_user_model()

class BreakSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Break
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    breaks = BreakSerializer(many=True, required=False)
    doctor = serializers.PrimaryKeyRelatedField(many=False, queryset=User.objects.filter(role=User.Types.DOCTOR).all(), required=True)

    class Meta:
        model = Schedule
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['doctor'] = UserSerializer(many=False)
        return super(ScheduleSerializer, self).to_representation(instance)

    def create(self, validated_data):
        breaks = validated_data.pop('breaks', []) 
        schedule = Schedule.objects.create(**validated_data)
        for b in breaks:
            obj = schedule.breaks.create(start_time=b.get('start_time'), end_time=b.get('end_time'))
            schedule.breaks.add(obj)
        schedule.save()
        return schedule

    def update(self, instance, validated_data):
        breaks = validated_data.pop('breaks', []) 
        
        if not self.partial:
            instance.breaks.clear()
        
        for b in breaks:
            obj = instance.breaks.create(start_time=b.get('start_time'), end_time=b.get('end_time'))
            instance.breaks.add(obj)

        [setattr(instance, k, v) for k, v in validated_data.items()]
        instance.save()
        return instance
        