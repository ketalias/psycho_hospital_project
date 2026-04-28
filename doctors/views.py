from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from rest_framework.generics import ListAPIView
from .models import Doctor
from .forms import DoctorForm
from .serializers import DoctorSerializer

class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctors/doctor_list.html'
    context_object_name = 'doctors'

class DoctorCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'doctors.add_doctor'
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctors/doctor_form.html'
    success_url = reverse_lazy('doctors:doctor_list')

class DoctorUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'doctors.change_doctor'
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctors/doctor_form.html'
    success_url = reverse_lazy('doctors:doctor_list')

class DoctorListAPIView(ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


