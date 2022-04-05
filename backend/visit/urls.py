from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('bills', views.BillViewSet)
router.register('visits', views.VisitViewSet)
router.register('payments', views.PaymentViewSet)
router.register('insurance', views.InsuranceViewSet)
router.register('prescriptions', views.PrescriptionViewSet)
