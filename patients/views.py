from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import PatientSerializer
from .models import Patient

# Create your views here.

class PatientcretaView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        serializer=PatientSerializer(data=request.data)
        if serializer.is_valid():
            user=request.user
            serializer.save(created_by=user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        user=request.user
        patients = Patient.objects.filter(created_by=user)
        serializer=PatientSerializer(patients,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class PatientdetailView2(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request, id):
        user = request.user
        try:
            patient = Patient.objects.get(id=id, created_by=user)
        except Patient.DoesNotExist:
            return Response({"message": "Patient not found"},status=status.HTTP_404_NOT_FOUND)
        serializer = PatientSerializer(patient)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self,request,id):
        user=request.user
        try:
            patient=Patient.objects.get(id=id,created_by=user)
        except Patient.DoesNotExist:
            return Response({'message':'patient not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer=PatientSerializer(patient,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,id):
        user=request.user
        try:
            patient=Patient.objects.get(id=id,created_by=user)
        except Patient.DoesNotExist:
            return Response({'messgae':'patient not found'},status=status.HTTP_404_NOT_FOUND)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        