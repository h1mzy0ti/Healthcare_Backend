"""
URL configuration for healthcare_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from user.views import *
from clinic.views import *

from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('api/auth/register/', RegisterView.as_view()),
    path('api/auth/login/', TokenObtainPairView.as_view()),

    # Patient
    path('api/patients/', PatientListCreateView.as_view()),
    path('api/patients/<int:id>/', PatientDetailView.as_view()),

    # Doctor
    path('api/doctors/', DoctorListCreateView.as_view()),
    path('api/doctors/<int:id>/', DoctorDetailView.as_view()),

    # Mapping
    path('api/mappings/', MappingListCreateView.as_view()),
    path('api/mappings/<int:patient_id>/', PatientMappingView.as_view()),
    path('api/mappings/delete/<int:id>/', MappingDeleteView.as_view()),
]