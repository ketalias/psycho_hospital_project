from django.db import models
from doctors.models import Doctor


class Appointment(models.Model):
    patient_full_name = models.CharField(max_length=255, verbose_name="ПІБ пацієнта")
    patient_birth_date = models.DateField(verbose_name="Дата народження")
    patient_phone = models.CharField(max_length=20, verbose_name="Телефон")
    complaints = models.TextField(verbose_name="Скарги")
    appointment_date = models.DateTimeField(verbose_name="Дата прийому")
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.PROTECT,
        related_name="appointments",
        verbose_name="Лікар",
    )
    diagnosis = models.CharField(max_length=255, verbose_name="Діагноз")
    treatment_description = models.TextField(verbose_name="Опис лікування")

    class Meta:
        verbose_name = "Запис до лікаря"
        verbose_name_plural = "Записи до лікаря"
        ordering = ["-appointment_date"]

    def __str__(self):
        return f"{self.patient_full_name} -> {self.doctor.full_name}"
