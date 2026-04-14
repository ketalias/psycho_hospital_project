from django.contrib import admin
from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("full_name", "specialization", "years_of_experience")
    list_filter = ("specialization", "years_of_experience")
    search_fields = ("full_name", "specialization")
