from .serializers import ScheduleSerializer, BreakSerializer
from rest_framework.viewsets  import  ModelViewSet
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers
from .models import Schedule, Break

class ScheduleViewSet(ModelViewSet):
    
    queryset = Schedule.objects.order_by('created').all()
    serializer_class = ScheduleSerializer
    filterset_fields = ['day', 'doctor']
    search_fields = ['doctor__first_name', 'doctor__last_name']
    ordering_fields = '__all__'

    @action(detail=True, methods=['put', 'delete'], url_path='breaks')
    def breaks(self, request, pk=None):
        'add breaks'
        instance = self.get_object()
        data = JSONParser().parse(request)

        if request.method =='PUT':

            serializer = BreakSerializer(data=data, many=True, context={"request": request})            
            serializer.is_valid(raise_exception=True)

            for b in serializer.validated_data:
                obj = instance.breaks.create(start_time=b.get('start_time'), end_time=b.get('end_time'))
                instance.breaks.add(obj)
            instance.save()

            return Response(serializer.data, status=201)

        if request.method =='DELETE':

            # create serializer to validate list of ids here

            for id in data:
                try:
                    obj = Break.objects.get(pk=id)
                    if obj in instance.breaks.all():obj.delete()
                except Break.DoesNotExist:
                    pass
                
            return Response(status=204)