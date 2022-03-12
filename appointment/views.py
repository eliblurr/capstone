from rest_framework.viewsets  import  ModelViewSet
from .serializers import AppointmentSerializer
from .models import Appointment

# class AvailableSlot(ModelViewSet, CustomPagination):
#     'to be used in doctor view'

#     @action(detail=True, methods=['get'])
#     def bulk(self, request):
#         obj = self.get_object()
        # articles = get_children(obj, request.GET.get('moderate', False))
        # serializer = ArticleSummarySerializer(articles, many=True, context={"request": request})
        # # return Response(serializer.data,status=status.HTTP_200_OK)
        # res = serializer.data
        # page = self.paginate_queryset(res)   
        # if page is not None:
        #     res = self.get_paginated_response(page).data      
        # return Response(res,status=status.HTTP_200_OK
        # objs = self.queryset.filter(pk__in=request.data)
        # if objs:
        #     objs.delete()
        # return Response('success', status=status.HTTP_204_NO_CONTENT)

class AppointmentViewSet(ModelViewSet):
    
    queryset = Appointment.objects.order_by('created').all()
    serializer_class = AppointmentSerializer
    filterset_fields = ['id', 'doctor']
    search_fields = ['doctor__first_name', 'doctor__last_name', 'doctor__other_names']
    ordering_fields = '__all__'

