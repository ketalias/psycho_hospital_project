from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Appointment

class AppointmentListView(ListView):
    model = Appointment
    template_name = 'appointments/appointment_list.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        queryset = super().get_queryset()
        diagnosis_query = self.request.GET.get('diagnosis')
        if diagnosis_query:
            queryset = queryset.filter(diagnosis__icontains=diagnosis_query)
        return queryset

class AppointmentDetailView(DetailView):
    model = Appointment
    template_name = 'appointments/appointment_detail.html'
    context_object_name = 'appointment'

