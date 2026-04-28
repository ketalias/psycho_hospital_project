from django.urls import path
from .views import DoctorListView

app_name = 'doctors'

urlpatterns = [
    path('', DoctorListView.as_view(), name='doctor_list'),
]
