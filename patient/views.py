from rest_framework.viewsets  import  ModelViewSet
from rest_framework.decorators import action
from .serializers import PatientSerializer
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, NotFound

from .models import Patient

from ghana_card.models import GhanaCard


class PatientViewSet(ModelViewSet):
    
    queryset = Patient.objects.order_by('created').all()
    serializer_class = PatientSerializer
    filterset_fields = ['id', 'nationality', 'ghana_card_number', 'sex',]
    search_fields = ['surname', 'first_name', 'last_name', 'other_names', 'nationality']
    ordering_fields = '__all__'
    M_FIELDS = ['surname', 'first_name', 'nationality', 'other_names', 'sex', 'date_of_birth', 'height']

    @action(detail=False, methods=['post', 'put'], url_path='ghana-card')
    def create_from_card_number(self, request, pk=None):
        card = request.query_params.get('card', None)
        if not card:raise ValidationError('card required', code=422)
        card = GhanaCard.objects.filter(personal_id_number=card).first()
        if not card:raise NotFound("Card Not found.")

        data = {'ghana_card_number':card.personal_id_number}
        data.update({k:v for k,v in card.__dict__.items() if k in self.M_FIELDS})

        if request.method=='POST':
            serializer = PatientSerializer(data=data, many=False, context={"request": request})                        

        if request.method=='PUT': 
            patient = Patient.objects.filter(ghana_card_number=card.personal_id_number).first()
            if not patient:raise NotFound("Patient Not found.")
            serializer = PatientSerializer(patient, data=data, context={"request": request})   
        
        serializer.is_valid(raise_exception=True)  
        serializer.save()       
        return Response(serializer.data, status=201)

            
