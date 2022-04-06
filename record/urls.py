from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('records', views.RecordViewSet)
router.register('prescriptions', views.PrescriptionViewSet)
