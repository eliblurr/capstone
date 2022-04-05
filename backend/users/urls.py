from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers
from django.urls import re_path
from . import views

router = routers.DefaultRouter()

router.register('users', views.UserViewSet)

urlpatterns = [
    re_path(r'register(/)?', views.UserRegistrationView.as_view(), name='register'), 
    re_path(r'token/obtain(/)?', TokenObtainPairView.as_view(), name='token_create'), # {'employee_id': <employee-id>, 'password': <password>}
    re_path(r'token/refresh(/)?', TokenRefreshView.as_view(), name='token_refresh'), # {'refresh': <jwt-token>}
    re_path(r'modify-users/?(?P<id>\w+)(/)?', views.UserView.as_view(), name='modify_users'),
    re_path(r'logout(/)?', views.LogOutView.as_view(), name='logout'),
    re_path(r'login(/)?', views.LoginView.as_view(), name='login'),
]