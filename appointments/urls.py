from django.urls import path
from .views import AppointmentListView, AppointmentDetailView, AppointmentCreateView, AppointmentUpdateView

app_name = 'appointments'

urlpatterns = [
    path('', AppointmentListView.as_view(), name='appointment_list'),
    path('add/', AppointmentCreateView.as_view(), name='appointment_add'),
    path('<int:pk>/', AppointmentDetailView.as_view(), name='appointment_detail'),
    path('<int:pk>/edit/', AppointmentUpdateView.as_view(), name='appointment_edit'),
]
