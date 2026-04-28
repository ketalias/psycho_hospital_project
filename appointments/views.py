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
        # Збереження фільтру в cookies
        if 'diagnosis' in request.GET:
            response.set_cookie('last_diagnosis_filter', request.GET.get('diagnosis'), max_age=60*60*24*30)
        return response

    def get_queryset(self):
        queryset = super().get_queryset()
        diagnosis_query = self.request.GET.get('diagnosis')
        
        # Читання з cookies, якщо немає в GET
        if diagnosis_query is None:
            diagnosis_query = self.request.COOKIES.get('last_diagnosis_filter')

        if diagnosis_query:
            queryset = queryset.filter(diagnosis__icontains=diagnosis_query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        diagnosis_query = self.request.GET.get('diagnosis')
        if diagnosis_query is None:
            diagnosis_query = self.request.COOKIES.get('last_diagnosis_filter', '')
        context['current_diagnosis_filter'] = diagnosis_query
        return context

class AppointmentDetailView(DetailView):
    model = Appointment
    template_name = 'appointments/appointment_detail.html'
    context_object_name = 'appointment'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        # Збереження в сесії
        appointment = self.get_object()
        request.session['last_viewed_appointment'] = {
            'id': appointment.id,
            'name': appointment.patient_full_name
        }
        return response

class AppointmentCreateView(CreateView):
    # Знято LoginRequiredMixin - доступно для всіх
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


