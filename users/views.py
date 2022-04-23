from .serializers import UserSerializer, LogOutSerializer, LoginSerializer
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import  APIView
from rest_framework import viewsets
from hms.cls import Aggregation
from .models import User

class UserViewSet(Aggregation, viewsets.ReadOnlyModelViewSet):
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

# https://medium.com/grad4-engineering/how-to-blacklist-json-web-tokens-in-django-43fb88ae3d17
class LogOutView(APIView):
    serializer_class = LogOutSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        refresh = serializer.data['refresh']   

        try:
            token = RefreshToken(refresh)
            token.blacklist()
        except TokenError as e:
            return Response(e.__str__(), status=400)

        return Response({
            'success': True,
            'statusCode': 200,
            'message': 'User logged out!',
        }, status=200)

class LoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        response = {
            'success': True,
            'statusCode': 200,
            'message': 'user logged in successfully',
            'access': serializer.data['access'],
            'refresh': serializer.data['refresh'],
            'user':  serializer.data['user']
        }

        return Response(response, status=200)

class UserView(Aggregation, APIView):

    serializer_class = UserSerializer

    def patch(self, request, id, format=None):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response('user not found', status=404)

        serializer = self.serializer_class(user, data=request.data, partial=True, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=202)

    def delete(self, request, id):
        try:
            user = User.objects.get(id=id)
            user.delete()
        except User.DoesNotExist:
            pass
        return Response(status=204)
