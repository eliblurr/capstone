from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('pharmacies', views.PharmacyViewSet)
router.register('drugs', views.DrugViewSet)
