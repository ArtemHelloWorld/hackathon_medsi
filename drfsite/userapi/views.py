from django.shortcuts import render
from rest_framework import generics, viewsets

from userapi.serializers import *


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class PatientDoctorViewSet(viewsets.ModelViewSet):
    queryset = PatientDoctor.objects.all()
    serializer_class = PatientDoctorSerializer



# class PatientAPIList(generics.ListCreateAPIView):
#     queryset = Patient.objects.all()
#     serializer_class = PatientSerializer
#
#
# class PatientAPIUpdate(generics.UpdateAPIView):
#     queryset = Patient.objects.all()
#     serializer_class = PatientSerializer
#
#
# class PatientAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Patient.objects.all()
#     serializer_class = PatientSerializer
