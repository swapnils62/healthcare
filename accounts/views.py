from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterSerializer

# Create your views here.

class Regiterview(APIView):
    def post(self, request):
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Register successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Loginview(APIView):
    def post(self, requset):
        username=requset.data.get('username')
        password=requset.data.get('password')

        user=authenticate(username=username, password=password)

        if user is None:
            return Response({'message':'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        refresh=RefreshToken.for_user(user)

        return Response({
            'refresh':str(refresh),
            'access_token':str(refresh.access_token)
        })