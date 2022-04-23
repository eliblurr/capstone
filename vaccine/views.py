from rest_framework.viewsets  import  ModelViewSet
from .serializers import VaccineSerializer
from hms.cls import Aggregation
from .models import Vaccine

class VaccineViewSet(Aggregation, ModelViewSet):
    
    queryset = Vaccine.objects.order_by('created').all()
    serializer_class = VaccineSerializer
    filterset_fields = ['id', 'name', 'recommended_dosage']
    search_fields = ['name', 'description']
    ordering_fields = '__all__'