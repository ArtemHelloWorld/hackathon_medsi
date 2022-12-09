from django.contrib.auth.models import AbstractUser, User
from django.db import models


class Patient(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    phone = models.CharField(max_length=15, null=True, blank=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return f'Patient {self.name} {self.surname}'


class Doctor(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    profession = models.TextField()
    phone = models.CharField(max_length=15, null=True, blank=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return f'Doctor {self.name} {self.surname}'


class PatientDoctor(models.Model):
    doctor_id = models.IntegerField(max_length=10)
    patient_id = models.IntegerField(max_length=10)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Doctor {self.doctor_id} - patient {self.patient_id}'

