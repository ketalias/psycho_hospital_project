from django import forms
from .models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['full_name', 'specialization', 'years_of_experience']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ПІБ лікаря'}),
            'specialization': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Спеціалізація'}),
            'years_of_experience': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
        }
