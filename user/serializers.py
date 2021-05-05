from rest_framework import  serializers
from rest_framework.permissions import IsAuthenticated
# from django.db import models
from .models import AddUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password# Register serializer

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddUser
        fields = ('id','username','email','password')

        def create(self, validated_data):
            user = AddUser.objects.create_user(
                id = validated_data['id'],
                username = validated_data['username'],
                email = validated_data['email'],    
                password = validated_data['password'],
            )
            return user# User serializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddUser
        fields = '__all__'




def validate_password(self, value: str) -> str:
    return make_password(value)
