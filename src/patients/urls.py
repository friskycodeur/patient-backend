from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView
from patient.views import patient_list_view

urlpatterns = [
    path("", patient_list_view, name="home"),
    path("admin/", admin.site.urls),
    path("patient/", include("patient.urls")),
]
