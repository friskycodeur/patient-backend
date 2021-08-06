from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.patient_create_view, name="patient-create"),
    path("list/", views.patient_list_view, name="patient-list"),
    path("update/<int:id>", views.patient_update_view, name="patient-update"),
    path("detail/<int:id>", views.patient_detail_view, name="patient-detail"),
    path("delete/<int:id>", views.patient_delete_view, name="patient-delete"),
]
