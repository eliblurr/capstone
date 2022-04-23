from .serializers import LabTestSerializer, TestTypeSerializer
from rest_framework.viewsets  import  ModelViewSet
from .models import LabTest, TestType
from hms.cls import Aggregation

class TestTypeViewSet(Aggregation, ModelViewSet):
    
    queryset = TestType.objects.order_by('created').all()
    serializer_class = TestTypeSerializer
    filterset_fields = ['id']
    search_fields = ['name', 'description']
    ordering_fields = '__all__'

class LabTestViewSet(Aggregation, ModelViewSet):
    
    queryset = LabTest.objects.order_by('created').all()
    serializer_class = LabTestSerializer
    filterset_fields = ['id', 'test_type', 'lab_technician']
    search_fields = ['test_type__name', 'test_type__description']
    ordering_fields = '__all__'