from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        "patient_full_name",
        "appointment_date",
        "doctor",
        "diagnosis",
    )
    list_filter = ("appointment_date", "doctor", "doctor__specialization")
    search_fields = ("patient_full_name", "patient_phone", "diagnosis", "doctor__full_name")
    autocomplete_fields = ("doctor",)
