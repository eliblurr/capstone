
from rest_framework import routers
from django.urls import re_path
from . import views

router = routers.DefaultRouter()

router.register('users', views.UserViewSet)

urlpatterns = [
    re_path(r'register(/)?', views.UserRegistrationView.as_view(), name='register'), 
]




























# router.register('lab-tests', views.LabTestViewSet)
# from .views import UserRegistrationView
# from django.urls import re_path

# # from rest_framework_simplejwt import views as jwt_views


# urlpatterns = [
# #     # re_path(r'token/obtain(/)?', jwt_views.TokenObtainPairView.as_view(),name='token_create'),
# #     # re_path(r'token/refresh(/)?', jwt_views.TokenRefreshView.as_view(),name='token_refresh'),
#     # re_path(r'register(/)?', views.UserRegistrationView.as_view(), name='register'),
# #     # re_path(r'users(/)?(?P<id>\w+)?', UserListView.as_view(), name='users'),
# #     # re_path(r'logout(/)?', UserLogOutView.as_view(), name='logout'),
# #     # re_path(r'login(/)?', UserLoginView.as_view(), name='login'),
# ]