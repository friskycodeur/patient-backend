from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="__base.html"), name="home"),
    path("admin/", admin.site.urls),
    path("patient/", include("patient.urls")),
]
