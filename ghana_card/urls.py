# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
# ]

# urlpatterns = [
#     path('ghana-card/', include(router.urls)),
# ]

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()

router.register('ghana-card', views.GhanaCardViewSet)
