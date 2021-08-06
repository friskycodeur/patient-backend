from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

# Create your views here.
from .models import Patient
from .forms import PatientForm


def patient_create_view(request):
    context = {}
    template_name = "patient_form.html"
    form = PatientForm(request.POST or None)

    if form.is_valid():
        form.save()

    context["form"] = form
    return render(request, template_name, context)


def patient_list_view(request):
    context = {}
    template_name = "patient_list.html"
    context["patients"] = Patient.objects.all()

    return render(request, template_name, context)


def patient_detail_view(request, id):
    context = {}
    template_name = "patient_detail.html"
    context["patient"] = Patient.objects.get(id=id)

    return render(request, template_name, context)


def patient_update_view(request, id):
    context = {}
    template_name = "patient_form.html"
    obj = get_object_or_404(Patient, id=id)
    form = PatientForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

    context["form"] = form

    return render(request, template_name, context)


def patient_delete_view(request, id):
    template_name = "patient_delete.html"
    obj = get_object_or_404(Patient, id=id)

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")

    return render(request, template_name)
