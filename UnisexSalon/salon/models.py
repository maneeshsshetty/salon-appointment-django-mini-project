# Create your models here.
from django.db import models

class Appointment(models.Model):
    SERVICE_CHOICES = [
        ('Haircut', 'Haircut'),
        ('Hair Coloring', 'Hair Coloring'),
        ('Manicure', 'Manicure'),
    ]

    customer_name = models.CharField(max_length=100)
    service = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    def __str__(self):
        return f"{self.customer_name} - {self.service} on {self.appointment_date} at {self.appointment_time}"

