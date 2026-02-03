from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import DoctorSerializer
from .models import Doctor

# Create your views here.

class Doctorcreateview(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        serializer=DoctorSerializer(data=request.data)
        if serializer.is_valid():
            user=request.user
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        doctors = Doctor.objects.all() 
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class Doctordetailview(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,id):
        try:
            doctor=Doctor.objects.get(id=id)
        except Doctor.DoesNotExist:
            return Response({'message':'doctor not found'},status=status.HTTP_404_NOT_FOUND)
        serializer=DoctorSerializer(doctor)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self, request,id):
        try:
            doctor=Doctor.objects.get(id=id)
        except Doctor.DoesNotExist:
            return Response({'message':'doctor not found '},status=status.HTTP_404_NOT_FOUND)
        serializer=DoctorSerializer(doctor,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        try:
            doctor=Doctor.objects.get(id=id)
        except Doctor.DoesNotExist:
            return Response({'message':'doctor not found'},status=status.HTTP_404_NOT_FOUND)
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)