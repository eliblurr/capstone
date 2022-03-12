from .serializers import PharmacySerializer, DrugSerializer
from rest_framework.viewsets  import  ModelViewSet
from .models import Pharmacy, Drug

class PharmacyViewSet(ModelViewSet):
    
    queryset = Pharmacy.objects.order_by('created').all()
    serializer_class = PharmacySerializer
    filterset_fields = ['id']
    search_fields = ['name', 'description']
    ordering_fields = '__all__'

class DrugViewSet(ModelViewSet):
    
    queryset = Drug.objects.order_by('created').all()
    serializer_class = DrugSerializer
    filterset_fields = ['id', 'pharmacy']
    search_fields = ['name', 'description']
    ordering_fields = '__all__'