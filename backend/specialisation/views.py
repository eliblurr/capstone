from rest_framework.viewsets  import  ModelViewSet
from .serializers import SpecialisationSerializer
from .models import Specialisation

class SpecialisationViewSet(ModelViewSet):
    
    queryset = Specialisation.objects.order_by('created').all()
    serializer_class = SpecialisationSerializer
    filterset_fields = ['id', 'name']
    search_fields = ['name', 'description']
    ordering_fields = '__all__'