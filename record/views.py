from .serializers import PrescriptionSerializer, RecordSerializer
from rest_framework.viewsets  import  ModelViewSet
from .models import Record, Prescription

class RecordViewSet(ModelViewSet):
    
    queryset = Record.objects.order_by('created').all()
    serializer_class = RecordSerializer
    filterset_fields = ['id', 'doctor', 'patient', 'diagnosis_type', 'record_type', 'date']
    search_fields = ['date', 'examination_finding_types', 'investigation_request', 'diagnosis']
    ordering_fields = '__all__'

class PrescriptionViewSet(ModelViewSet):
    
    queryset = Prescription.objects.order_by('created').all()
    serializer_class = PrescriptionSerializer
    filterset_fields = ['id',  'status', 'issued_by', 'record']
    search_fields = ['drug__name', 'drug__description']
    ordering_fields = '__all__'
