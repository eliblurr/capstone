from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('lab-test-types', views.TestTypeViewSet)
router.register('lab-tests', views.LabTestViewSet)
