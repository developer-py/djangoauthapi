from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView 
from account.serializers import UserRegistationSerialiazer,UserLoginSerialiazer 
# Create your views here.
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from social_django.utils import psa
from django.shortcuts import render 
from allauth.socialaccount.models import SocialAccount
# generet manualy token
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'access': str(refresh.access_token),
        'refresh': str(refresh),
    }

class UserRegistrationView(APIView):

    def get(self,request,format=None):
        return Response({'msg':'get data'})

    def post(self,request,format=None):
        serialiazer=UserRegistationSerialiazer(data=request.data)
        if serialiazer.is_valid(raise_exception=True):
            user=serialiazer.save()
            # token=get_tokens_for_user(user)
            return Response({'msg':'Registration Success'},status=status.HTTP_201_CREATED)
        return Response(serialiazer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class UserLoginView(APIView):
    def post(self,request,format=None):
        serialiazer=UserLoginSerialiazer(data=request.data)
        if serialiazer.is_valid(raise_exception=True):                                                                                                                                                                                                                                                                                              
            email=serialiazer.data.get('email')
            password=serialiazer.data.get('password')
            user=authenticate(email=email,password=password)
            if user is not None:    
                token=get_tokens_for_user(user)
                return Response({'token':token,'msg':"Login Success"},status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['Email or Password is not valid']}},status=status.HTTP_404_NOT_FOUND)
        return Response(serialiazer.errors,status=status.HTTP_400_BAD_REQUEST)
    





