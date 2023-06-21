"""whip URL Configuration

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
import os
from django.urls import path, include
from django.http import FileResponse
from django.conf import settings
from django.contrib import admin
from django.views.generic import View

from . import views

class WellKnownView(View):
    def get(self, request, file_path):
        file = os.path.join(settings.BASE_DIR, '.well-known', file_path)
        return FileResponse(open(file, 'rb'))

class ACME(View):
    def get(self, request, file_path):
        file = os.path.join(settings.BASE_DIR, '.well-known/acme-challenge', file_path)
        return FileResponse(open(file, 'rb'))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Gestational_Limits/', views.whip_gestational_limits_API),
    path('Insurance_Coverage/', views.whip_insurance_coverage_API),
    path('Minors/', views.whip_minors_API),
    path('Waiting_Period/', views.whip_waiting_period_API),
    path('.well-known/<path:file_path>', WellKnownView.as_view()),
    path('.well-known/acme-challenge/<path:file_path>', ACME.as_view()),    
]