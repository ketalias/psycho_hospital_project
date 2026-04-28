from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'patient_full_name', 'patient_birth_date', 'patient_phone', 
            'complaints', 'appointment_date', 'doctor', 'diagnosis', 
            'treatment_description'
        ]
        widgets = {
            'patient_full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ПІБ пацієнта'}),
            'patient_birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'patient_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+380...'}),
            'complaints': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Опис скарг'}),
            'appointment_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'doctor': forms.Select(attrs={'class': 'form-control'}),
            'diagnosis': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Попередній або остаточний діагноз'}),
            'treatment_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Призначення та лікування'}),
        }
