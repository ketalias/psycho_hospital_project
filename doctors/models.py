from django.db import models


class Doctor(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ПІБ")
    specialization = models.CharField(max_length=255, verbose_name="Спеціалізація")
    years_of_experience = models.PositiveIntegerField(verbose_name="Стаж (років)")

    class Meta:
        verbose_name = "Лікар"
        verbose_name_plural = "Лікарі"
        ordering = ["full_name"]

    def __str__(self):
        return f"{self.full_name} ({self.specialization})"
