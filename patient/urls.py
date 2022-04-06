from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('patients', views.PatientViewSet)
router.register('allergies', views.AllergyViewSet)
