from rest_framework.viewsets  import  ModelViewSet
from .serializers import RecordsSerializer
from .models import Records

class RecordsViewSet(ModelViewSet):
    
    queryset = Records.objects.order_by('created').all()
    serializer_class = RecordsSerializer
    filterset_fields = ['patient_id', 'name_of_patient']
    search_fields = ['name_of_patient']
    ordering_fields = '__all__'