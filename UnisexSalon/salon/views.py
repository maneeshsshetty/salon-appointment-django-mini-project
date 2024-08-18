# Create your views here.
from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm

def schedule_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            if Appointment.objects.filter(appointment_date=appointment.appointment_date,
                                          appointment_time=appointment.appointment_time).exists():
                error_message = "Collision detected! Appointment not scheduled."
                return render(request, 'salon/schedule.html', {'form': form, 'error_message': error_message})
            appointment.save()
            return redirect('view_appointments')
    else:
        form = AppointmentForm()
    return render(request, 'salon/schedule.html', {'form': form})

def view_appointments(request):
    appointments = Appointment.objects.all().order_by('appointment_date', 'appointment_time')
    return render(request, 'salon/view.html', {'appointments': appointments})
