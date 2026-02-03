from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import PDmapSerializer
from doctors.models import Doctor
from patients.models import Patient
from .models import PatientDoctorMapping

# Create your views here.

class DoctormapPatient(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        serializer=PDmapSerializer(data=request.data)
        if serializer.is_valid():
            patient=serializer.validated_data['patient']
            if patient.created_by != request.user:
                return Response({'message':'You cannot assign doctors to this patient'},status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        mappings = PatientDoctorMapping.objects.all()
        serializer = PDmapSerializer(mappings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class PDByPatientView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            patient = Patient.objects.get(id=id,created_by=request.user)
        except Patient.DoesNotExist:
            return Response({"message": "Patient not found"},status=status.HTTP_404_NOT_FOUND)

        mappings = PatientDoctorMapping.objects.filter(patient=patient)
        serializer = PDmapSerializer(mappings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        try:
            mapping = PatientDoctorMapping.objects.get(id=id)
        except PatientDoctorMapping.DoesNotExist:
            return Response({"message": "Mapping not found"},status=status.HTTP_404_NOT_FOUND)
        
        if mapping.patient.created_by != request.user:
            return Response({"message": "Not allowed"},status=status.HTTP_403_FORBIDDEN)

        mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)