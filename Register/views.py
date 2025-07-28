from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Register.models import User, userProfile, verificationCode
from .serializer import UserSerializer, userProfileSerializer, verificationCodeSerializer
from rest_framework import generics

# Create your views here.
#  1
# def fullname (request):
#     fname = input("Enter your first name:")
#     lname = input("Enter your last name:")
#     return HttpResponse (f'Your fullname is: {fname} {lname}')

# or 2

# def fullname (request):
#     first_name = "Hadiqe"
#     last_name = "mahdavi"
#     return HttpResponse (f'Your fullname is: {first_name} {last_name}')

#or 3

# def fullname (request, first, last):
#      return HttpResponse(f"First Name: {first}, Last Name: {last}")



class UserCreateView(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many = True)
        return Response (serializer.data)
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
      

class userProfileSerializerview(generics.ListCreateAPIView):
    queryset = userProfile.objects.all()
    serializer_class = userProfileSerializer

class verificationCodeSerializerview(generics.ListCreateAPIView):
    queryset = verificationCode.objects.all()
    serializer_class = verificationCodeSerializer