from rest_framework.viewsets  import  ModelViewSet
from .serializers import GhanaCardSerializer
from .models import GhanaCard

class GhanaCardViewSet(ModelViewSet):
    
    queryset = GhanaCard.objects.order_by('created').all()
    serializer_class = GhanaCardSerializer
    filterset_fields = ['id', 'nationality', 'personal_id_number', 'sex', 'document_number',]
    search_fields = ['surname', 'first_name', 'previous_names', 'nationality']
    ordering_fields = '__all__'