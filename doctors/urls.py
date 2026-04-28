from django.urls import path
from .views import DoctorListView, DoctorCreateView, DoctorUpdateView, DoctorListAPIView

app_name = 'doctors'

urlpatterns = [
    path('', DoctorListView.as_view(), name='doctor_list'),
    path('add/', DoctorCreateView.as_view(), name='doctor_add'),
    path('<int:pk>/edit/', DoctorUpdateView.as_view(), name='doctor_edit'),
    path('api/doctors/', DoctorListAPIView.as_view(), name='api_doctor_list'),
]
