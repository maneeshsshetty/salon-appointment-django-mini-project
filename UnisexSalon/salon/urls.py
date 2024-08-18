from django.urls import path
from . import views

urlpatterns = [
    path('', views.schedule_appointment, name='schedule_appointment'),
    path('appointments/', views.view_appointments, name='view_appointments'),
]
