from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('records', views.RecordViewSet)
router.register('prescriptions', views.PrescriptionViewSet)
router.register('request-records', views.RecordRequestViewSet)
router.register('vitals', views.VitalsViewSet)