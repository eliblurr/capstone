from .utils import date_range, combine_dt_time, get_free_epochs
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets  import  ModelViewSet
from .serializers import AppointmentSerializer
from django.contrib.auth import get_user_model
from users.serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from schedule.models import Schedule
from .models import Appointment
from datetime import timedelta

User = get_user_model()

class AppointmentViewSet(ModelViewSet):
    
    queryset = Appointment.objects.order_by('created').all()
    serializer_class = AppointmentSerializer
    filterset_fields = ['id', 'doctor']
    search_fields = ['doctor__first_name', 'doctor__last_name', 'doctor__other_names']
    ordering_fields = '__all__'

    @action(detail=False, methods=['get'], url_path='available-epochs', name='Free Appointment Slots', basename='kjhfgds')
    def get_free_epochs(self, request):
        params = request.query_params
        start, end, duration, doctor, specialisation, epochs = params.get('start',''), params.get('end',''),\
        params.get('duration',30), params.get('doctor', None), params.get('specialisation', None), {}

        if start=='' or end=='':raise ValidationError('start and end required', code=400)

        try: dt_range, duration = date_range(start, end), int(duration) 
        except Exception as e: raise  ValidationError(e, code=400)

        doctors = User.objects.all().filter(role=User.Types.DOCTOR)

        if specialisation: doctors = doctors.filter(doctor__specialisation__exact=specialisation)
        if doctor: doctors = doctors.filter(pk__exact=doctor) 
        
        for date in dt_range:
                epochs.update({f'{date}':[]})
                for doctor in doctors:
                        schedule = Schedule.objects.all().filter(doctor=doctor, day=date.weekday()).first()
                        appointments = Appointment.objects.all().filter(doctor=doctor, date__exact=date, status__in=['booked', 'confirmed'])
                        
                        if not schedule:continue
                        
                        ex_epochs = list(appointments.values()) + list(schedule.breaks.all().values())
                        ex_epochs = [(combine_dt_time(date, epoch["start_time"]), combine_dt_time(date, epoch["end_time"]), ) for epoch in ex_epochs]
                                                
                        start_time, end_time = combine_dt_time(date, schedule.start_time), combine_dt_time(date, schedule.end_time)
                        
                        available_epochs = get_free_epochs((start_time, end_time), ex_epochs, timedelta(minutes=duration))
                        
                        doctor = UserSerializer(doctor, context={'request':request})
                        epochs[f'{date}'].append({'doctor':doctor.data, 'epochs':available_epochs})

        # /appointments/available-epochs/?duration=45&start=2022-03-18&end=2022-03-19&doctor=1&specialisation=1  -> duration in minutes

        return Response(epochs, status=200)
