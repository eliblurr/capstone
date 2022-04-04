from rest_framework.response import Response
from rest_framework.views import  APIView
from .serializers import UserSerializer
from rest_framework import viewsets
from .models import User

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.order_by('id').all()
    serializer_class = UserSerializer

class UserRegistrationView(APIView):
    serializer_class = UserSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            serializer.save()

            response = {
                'success': True,
                'statusCode': 201,
                'message': 'User successfully registered!',
                'user': serializer.data
            }

            return Response(response, status=201)


    # def get(self, request, format=None):
    #     """
    #     Return a list of all users.
    #     """
    #     usernames = [user.username for user in User.objects.all()]
    #     return Response(usernames)








































































# from .serializers import ProfileSerializer, UserSerializer, ProfileTypeSerializer
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from .models import ProfileType, User, Profile, Region, District
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework_simplejwt.exceptions import TokenError
# from rest_framework_simplejwt.tokens import RefreshToken
# from theme.views import IsAdmin, IsOwner, ReadOnly
# from rest_framework.viewsets  import  ModelViewSet
# from reports.serializers import ReportSerializer
# from django.contrib.auth import get_user_model
# from msmes.paginition import CustomPagination
# from rest_framework.response import Response
# from rest_framework.decorators import action
# from rest_framework.views import  APIView
# from rest_framework import filters,status
# from forum.views import BulkOp
# from .serializers import *
# from fts.views import FTS

# User = get_user_model()

# class RegionViewSet(BulkOp, FTS, ModelViewSet):
#     permission_classes = [IsAdmin|ReadOnly]
#     queryset = Region.objects.all()
#     serializer_class = RegionSerializer
#     filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
#     filterset_fields = ['id', 'name', 'slug']
#     search_fields = ['name', 'slug']
#     ordering_fields = '__all__'
#     fts_search_fields = ['name','slug']

# class DistricViewSet(BulkOp, FTS, ModelViewSet):
#     permission_classes = [IsAdmin|ReadOnly]
#     queryset = District.objects.all()
#     serializer_class = DistrictSerializer
#     filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
#     filterset_fields = ['id', 'name', 'slug']
#     search_fields = ['name', 'slug']
#     ordering_fields = '__all__'
#     fts_search_fields = ['name','slug','region__name','region__slug']

# class ProfileTypeViewSet(ModelViewSet):
#     """
#     API endpoint that allows profiles to be viewed or edited.
#     """
#     permission_classes = [IsAdmin|ReadOnly]
#     queryset = ProfileType.objects.all()
#     serializer_class = ProfileTypeSerializer
#     filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
#     filterset_fields = ['id', 'name']
#     search_fields = ['name']
#     ordering_fields = '__all__'

# class ProfileViewSet(ModelViewSet):
#     """
#     API endpoint that allows profiles to be viewed or edited.
#     """
#     permission_classes = [IsAdmin|IsOwner|ReadOnly]
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
#     filterset_fields = ['id', 'name', 'profile_type', 'district', 'user']
#     ordering_fields = '__all__'

# class UserLoginView(APIView):
#     serializer_class = UserLoginSerializer
#     permission_classes = (AllowAny,)

#     def post(self, request, format=None):
#         serializer = self.serializer_class(data=request.data)
#         valid = serializer.is_valid(raise_exception=True)

#         if valid:

#             response = {
#                 'success': True,
#                 'statusCode': status.HTTP_200_OK,
#                 'message': 'User logged in successfully',
#                 'access': serializer.data['access'],
#                 'refresh': serializer.data['refresh'],
#                 'user': {
#                     'id': serializer.data['id'],
#                     'email': serializer.data['email'],
#                     'role': serializer.data['role'],
#                     'is_active': serializer.data['is_active'],
#                     'avatar': serializer.data['avatar'],
#                     'profile_id':serializer.data['profile']
#                 }
#             }

#             return Response(response, status=status.HTTP_200_OK)

# class UserRegistrationView(APIView):
#     serializer_class = UserSerializer
#     permission_classes = (AllowAny,)

#     def post(self, request, format=None):
#         serializer = self.serializer_class(data=request.data)
#         valid = serializer.is_valid(raise_exception=True)

#         if valid:
#             serializer.save()
#             status_code = status.HTTP_201_CREATED

#             response = {
#                 'success': True,
#                 'statusCode': status_code,
#                 'message': 'User successfully registered!',
#                 'user': serializer.data
#             }

#             return Response(response, status=status_code)

# class UserListView(APIView, CustomPagination):
#     serializer_class = UserListSerializer
#     authentication_classes = [JWTAuthentication]
#     permission_classes = (IsAdmin|IsOwner,) # IsAuthenticated

#     @action(detail=True, methods=['post','patch','put'], permission_classes=[IsAuthenticated]) 
#     def report(self, request, pk=None): 
#         user, author = self.get_object(), request.user

#         serializer = ReportSerializer(data=request.data)
#         if serializer.is_valid():
#             try:
#                 obj.report(author, serializer.data['reason'])
#                 obj.save()
#             except Exception as e:
#                 return Response(e.__str__(),status=status.HTTP_400_BAD_REQUEST)
            
#             res = ReportSerializer(obj.get_report(author), context={"request": request})
#             return Response({'object':res.data, 'user_has_reported': obj.user_has_reported(author)})
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     @action(detail=True, methods=['post','patch','put'], permission_classes=[IsAdmin])
#     def blacklist(self, request, pk=None, include_report=False):
#         user = self.get_object()
#         with transaction.atomic():
#             user.is_blacklisted = True
#             if include_report:user.deactivate_report()
#             user.save()

#         res = self.serializer_class(user, many=False, context={"request": request})
#         return Response(res.data)

#     @action(detail=True, methods=['post','patch','put'], permission_classes=[IsAdmin])
#     def whitelist(self, request, pk=None, include_report=False):
#         user = self.get_object()
#         with transaction.atomic():
#             user.is_blacklisted = False
#             user.save()
#         res = self.serializer_class(user, many=False, context={"request": request})
#         return Response(res.data)
            
#     @action(detail=True, methods=['patch'], permission_classes=[IsAdmin|IsOwner])
#     def deactivate(self, request, pk=None):
#         user = self.get_object()
#         case = ((user==request.user),(request.user.role in ['admin']))
#         if not any(case):
#             return Response('permission denied', status=403)
#         with transaction.atomic():
#             user.is_active = False
#             user.save()
#         res = self.serializer_class(user, many=False, context={"request": request})
#         return Response(res.data)
        
#     @action(detail=True, methods=['patch'], permission_classes=[IsAdmin|IsOwner]) 
#     def activate(self, request, pk=None):
#         user = self.get_object()
#         case = ((user==request.user),(request.user.role in ['admin']))
#         if not any(case):
#             return Response('permission denied', status=403)
#         with transaction.atomic():
#             user.is_active = True
#             user.save()
#         res = self.serializer_class(user, many=False, context={"request": request})
#         return Response(res.data)

#     def get(self, request, id=None, format=None):
#         user = request.user
#         if user.role in ['reporter','editor','service']:
#             response = {
#                 'success': False,
#                 'status_code': status.HTTP_403_FORBIDDEN,
#                 'message': 'You are not authorized to perform this action'
#             }
#             return Response(response, status.HTTP_403_FORBIDDEN)
#         else:
#             if id:
#                 try:
#                     user = UserSerializer(User.objects.get(id=id), context={"request": request})
#                     return Response(user.data, status=status.HTTP_200_OK)
#                 except User.DoesNotExist:
#                     return Response('resource not found', status=404)
            
#             moderate = self.request.query_params.get('moderate') in ['True','true',1, '1', True]

#             qs = User.objects.all() 
            
#             if user.role in ['admin'] and moderate:
#                 qs = qs
#             else:
#                 qs = qs.filter(is_active=True, is_blacklisted=False)

#             serializer = self.serializer_class(qs, many=True)
        
#             res = serializer.data

#             page = self.paginate_queryset(res, request=request)   
#             if page is not None:
#                 res = self.get_paginated_response(page).data      
#             return Response(res, status=status.HTTP_200_OK)

#     def patch(self, request, id, format=None):
#         try:
#             user = User.objects.get(id=id)
#         except User.DoesNotExist:
#             return Response('resource not found', status=404)

#         case = ((user==request.user),(request.user.role in ['admin']))

#         if not any(case):
#             return Response('permission denied', status=403)

#         serializer = UserSerializer(user, data=request.data, partial=True, context={"request": request})
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return  Response(serializer.data, status=202)

#     def delete(self, request, id):
#         try:
#             user = User.objects.get(id=id)
            
#             case = ((user==request.user),(request.user.role in ['admin']))
#             if not any(case):
#                 return Response('permission denied', status=403)
            
#             user.delete()
#         except User.DoesNotExist:
#             pass
#         return Response(status=204)

# class UserLogOutView(APIView):
#     serializer_class = UserLogOutSerializer

#     def post(self, request, format=None):
#         serializer = self.serializer_class(data=request.data)
#         valid = serializer.is_valid(raise_exception=True)

#         if valid:
#             refresh = serializer.data['refresh']            
#             try:
#                 token = RefreshToken(refresh)
#                 token.blacklist()
#             except TokenError as e:
#                 return Response(e.__str__(), status=status.HTTP_400_BAD_REQUEST)

#             return Response({
#                 'success': True,
#                 'statusCode': status.HTTP_200_OK,
#                 'message': 'User logged out!',
#             }, status=status.HTTP_200_OK)