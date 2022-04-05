"""hms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from specialisation.urls import router as specialisation
from appointment.urls import router as appointment
from ghana_card.urls import router as ghana_card
from pharmacy.urls import router as pharmacy
from schedule.urls import router as schedule
from vaccine.urls import router as vaccine
from patient.urls import router as patient
from visit.urls import router as visit
from users.urls import router as user
from lab.urls import router as lab
from rest_framework import routers

class DefaultRouter(routers.DefaultRouter):
    def extend(self, router):
        self.registry.extend(router.registry)

router = DefaultRouter()

router.extend(specialisation)
router.extend(appointment)
router.extend(ghana_card)
router.extend(pharmacy)
router.extend(schedule)
router.extend(vaccine)
router.extend(patient)
router.extend(visit)
router.extend(user)
router.extend(lab)

from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),    
    path('', include('users.urls')),
]
