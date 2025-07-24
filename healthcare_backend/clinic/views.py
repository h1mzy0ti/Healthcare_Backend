from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Patient, Doctor, PatientDoctorMapping
from .serializers import PatientSerializer, DoctorSerializer, MappingSerializer
from django.shortcuts import get_object_or_404

# ------------------- Patients -------------------

class PatientListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        patients = Patient.objects.filter(created_by=request.user)
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        return get_object_or_404(Patient, pk=pk, created_by=user)

    def get(self, request, id):
        patient = self.get_object(id, request.user)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    def put(self, request, id):
        patient = self.get_object(id, request.user)
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        patient = self.get_object(id, request.user)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ------------------- Doctors -------------------

class DoctorListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoctorDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Doctor, pk=pk)

    def get(self, request, id):
        doctor = self.get_object(id)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

    def put(self, request, id):
        doctor = self.get_object(id)
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        doctor = self.get_object(id)
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ------------------- Mappings -------------------

class MappingListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        mappings = PatientDoctorMapping.objects.all()
        serializer = MappingSerializer(mappings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MappingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(assigned_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MappingView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, patient_id):
        mappings = PatientDoctorMapping.objects.filter(patient_id=patient_id)
        serializer = MappingSerializer(mappings, many=True)
        return Response(serializer.data)


class MappingDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        mapping = get_object_or_404(PatientDoctorMapping, id=id)
        mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)