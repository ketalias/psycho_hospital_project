import urllib.parse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Appointment
from .forms import AppointmentForm

class AppointmentListView(ListView):
    model = Appointment
    template_name = 'appointments/appointment_list.html'
    context_object_name = 'appointments'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        if 'diagnosis' in request.GET:
            encoded_val = urllib.parse.quote(request.GET.get('diagnosis'))
            response.set_cookie('last_diagnosis_filter', encoded_val, max_age=60*60*24*30)
        return response

    def get_queryset(self):
        queryset = super().get_queryset()
        diagnosis_query = self.request.GET.get('diagnosis')
        
        if diagnosis_query is None:
            cookie_val = self.request.COOKIES.get('last_diagnosis_filter')
            if cookie_val:
                diagnosis_query = urllib.parse.unquote(cookie_val)

        if diagnosis_query:
            query_lower = diagnosis_query.lower()
            matching_ids = [
                app.id for app in queryset 
                if app.diagnosis and query_lower in app.diagnosis.lower()
            ]
            queryset = queryset.filter(id__in=matching_ids)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        diagnosis_query = self.request.GET.get('diagnosis')
        if diagnosis_query is None:
            cookie_val = self.request.COOKIES.get('last_diagnosis_filter')
            diagnosis_query = urllib.parse.unquote(cookie_val) if cookie_val else ''
        context['current_diagnosis_filter'] = diagnosis_query
        return context

class AppointmentDetailView(DetailView):
    model = Appointment
    template_name = 'appointments/appointment_detail.html'
    context_object_name = 'appointment'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        appointment = self.get_object()
        request.session['last_viewed_appointment'] = {
            'id': appointment.id,
            'name': appointment.patient_full_name
        }
        return response

class AppointmentCreateView(CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointments/appointment_form.html'
    success_url = reverse_lazy('appointments:appointment_list')

class AppointmentUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'appointments.change_appointment'
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointments/appointment_form.html'
    success_url = reverse_lazy('appointments:appointment_list')


