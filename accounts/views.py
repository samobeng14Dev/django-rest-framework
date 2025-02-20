from django.shortcuts import render
from django.contrib.auth import authenticate
from .serializers import SignUpSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.views import APIView

# Create your views here.


from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .serializers import SignUpSerializer
from .models import User


class SignUpView(APIView):
    permission_classes = [AllowAny]  # Allows anyone to access

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(
                user=user)  #  Generate Token
            return Response({"message": "User created", "token": token.key}, status=201)
        return Response(serializer.errors, status=400)


class LoginView(APIView):
    permission_classes = [AllowAny]  # Allow anyone to access login

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(email=email, password=password)

        if user is not None:
            response={"message":"User logged in successfully","user":str(user),"token":str(user.auth_token.key)}
            return Response(data=response,status=status.HTTP_200_OK)
        else:
            return Response({"message":"Invalid credentials"},status=status.HTTP_400_BAD_REQUEST)
   
    def get(self, request):
        """Returns user details if already logged in"""
        content={"user":str(request.user),"auth":str(request.auth)}
        return Response(data=content,status=status.HTTP_200_OK)