from .serializers import BillSerializer, VisitSerializer, InsuranceSerializer, PaymentSerializer #, PrescriptionSerializer
from .models import Bill, Visit, Payment, Insurance #, Prescription
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets  import  ModelViewSet
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from hms.cls import Aggregation


class VisitViewSet(ModelViewSet):
    
    queryset = Visit.objects.order_by('created').all()
    serializer_class = VisitSerializer
    filterset_fields = ['id', 'doctor', 'appointment', 'patient']
    search_fields = ['doctor__first_name', 'doctor__last_name', 'patient__first_name', 'patient__last_name', 'patient__other_names']
    ordering_fields = '__all__'

    @action(detail=True, methods=['delete', 'put'], url_path='prescriptions')
    def prescriptions(self, request, pk=None):
        instance = self.get_object()
        data = JSONParser().parse(request)

        if request.method =='PUT':

            serializer = PrescriptionSerializer(data=data, many=True, context={"request": request})            
            serializer.is_valid(raise_exception=True)

            for data in serializer.validated_data:
                data.update({'visit':instance})

            serializer.save()

            return Response(serializer.data, status=201)

        if request.method =='DELETE':

            # create serializer to validate list of ids here

            for id in data:
                try:
                    obj = Prescription.objects.get(pk=id, bill=instance.id)
                    obj.delete()
                except Prescription.DoesNotExist:
                    pass
                
            return Response(status=204)

class BillViewSet(Aggregation, ModelViewSet):
    
    queryset = Bill.objects.order_by('created').all()
    serializer_class = BillSerializer
    filterset_fields = ['id']
    ordering_fields = '__all__'

    @action(detail=True, methods=['put', 'delete'], url_path='payments')
    def payment(self, request, pk=None):
        instance = self.get_object()
        data = JSONParser().parse(request)

        if request.method =='PUT':

            amount = request.query_params.get('amount', None)

            if not amount:
                raise ValidationError('amount required', code=422)

            try: payment = instance.make_payment(amount)
            except Exception as e: raise  ValidationError(e, code=400)

            instance.save()

            payment = PaymentSerializer(payment, context={'request':request})

            return Response(payment.data, status=201)

        if request.method =='DELETE':

            # create serializer to validate list of ids here

            for id in data:
                try:
                    obj = Payment.objects.get(pk=id, bill=instance.id)
                    obj.delete()
                except Payment.DoesNotExist:
                    pass
                
            return Response(status=204)

class InsuranceViewSet(Aggregation, ModelViewSet):
    
    queryset = Insurance.objects.order_by('created').all()
    serializer_class = InsuranceSerializer
    filterset_fields = ['id', 'name']
    search_fields = ['name', 'description']
    ordering_fields = '__all__'

class PaymentViewSet(Aggregation, ModelViewSet):
    
    queryset = Payment.objects.order_by('created').all()
    serializer_class = PaymentSerializer
    filterset_fields = ['id', 'bill']
    ordering_fields = '__all__'
    http_method_names = ['get', 'put', 'patch']

# class PrescriptionViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     This viewset automatically provides `list` and `retrieve` actions.
#     """
#     queryset = Prescription.objects.order_by('created').all()
#     serializer_class = PrescriptionSerializer
#     filterset_fields = ['id',  'status', 'issued_by', 'visit'] #'drug', , 'drug__pharmacy'
#     search_fields = ['drug__name', 'drug__description']
#     ordering_fields = '__all__'
