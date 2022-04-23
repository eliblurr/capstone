from .serializers import PrescriptionSerializer, RecordSerializer, RecordRequestSerializer
from hms.settings import SECRET_KEY, RECORD_REQUEST_BASE_URL
from .models import Record, Prescription, RecordRequest
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets  import  ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.mail import send_mail
from hms.cls import Aggregation
from datetime import datetime
import jwt

class RecordViewSet(Aggregation, ModelViewSet):
    
    queryset = Record.objects.order_by('created').all()
    serializer_class = RecordSerializer
    filterset_fields = ['id', 'doctor', 'patient', 'diagnosis_type', 'record_type', 'date']
    search_fields = ['date', 'examination_finding_types', 'investigation_request', 'diagnosis']
    ordering_fields = '__all__'

    @action(detail=False, methods=['get'], url_path='transfer')
    def transfer(self, request):
        auth = request.query_params.get('auth', None)

        if not auth:
            raise ValidationError('missing token')

        data = jwt.decode(auth, SECRET_KEY, algorithms="HS256")

        if data['expires']:
            try:
                expires = datetime.strptime(data['expires'], '%Y-%m-%d')
            except Exception as e:
                raise ValidationError('something went wrong, token data format mismatch')

            if not expires > datetime.now():
                raise ValidationError('token expired')

        try:
            req = RecordRequest.objects.get(id=data['id']) 
            records = self.queryset.filter(created__date__range=[req.start_date, req.end_date]).all()
            
            serializer = self.serializer_class(records, many=True, context={'request':request})  
            
            res = serializer.data
            page = self.paginate_queryset(res)   
            if page is not None:
                res = self.get_paginated_response(page).data      
            return Response(res, status=200)

        except RecordRequest.DoesNotExist:
            raise ValidationError('could not find request for token')
        except Exception as e:
            raise ValidationError(f'{e}')        
    
class PrescriptionViewSet(Aggregation, ModelViewSet):
    
    queryset = Prescription.objects.order_by('created').all()
    serializer_class = PrescriptionSerializer
    filterset_fields = ['id',  'status', 'issued_by', 'record']
    search_fields = ['drug__name', 'drug__description']
    ordering_fields = '__all__'

class RecordRequestViewSet(Aggregation, ModelViewSet):
    
    queryset = RecordRequest.objects.order_by('created').all()
    serializer_class = RecordRequestSerializer
    filterset_fields = ['id',  'status', 'record_type', 'ghana_card_no']
    http_method_names = ['get', 'post', 'head', 'delete']
    search_fields = ['name', 'subdomain_id']
    ordering_fields = '__all__'

    @action(detail=True, methods=['post'], url_path='decline')
    def decline(self, request, pk=None):
        obj = self.get_object()
        obj.status = RecordRequest.Status.DECLINED
        obj.save()
        
        try:
            send_mail(
                'Your request has been declined',
                f'Your request for patient with ghana card number {obj.ghana_card_no} has been declined.',
                'from@example.com',
                [obj.email],
                fail_silently=False,
            )
        except Exception as e:
            raise ValidationError('something went wrong')

        

        return Response('success', 200)

    @action(detail=True, methods=['post'], url_path='accept')
    def accept(self, request, pk=None):

        obj = self.get_object()

        expires, data = request.query_params.get('expires', None), {"id": obj.id, 'expires':None}
        if expires:
            try:
                datetime.strptime(expires, '%Y-%m-%d')
            except Exception as e:
                raise ValidationError('date object should match format %Y-%m-%d')
            
            data['expires'] = expires

        encoded = jwt.encode(data, SECRET_KEY, algorithm="HS256")
        obj.status = RecordRequest.Status.ACCEPTED
        obj.save()

        try:
            send_mail(
                'Request link',
                f'Visit the link below to see data '
                f'{RECORD_REQUEST_BASE_URL}?auth={encoded}',
                'from@example.com',
                [obj.email],
                fail_silently=False,
            )
        except Exception as e:
            raise ValidationError('something went wrong')

        return Response('success', 200)
