# from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import viewsets
from .models import AddUser
from .serializers import UserSerializer

class UserView(APIView):
    def post(self, request, *args, **kwargs):
        data = {
                'id': request.data.get('id'),
                'username': request.data.get('username'),
                'email': request.data.get('email'),
                'password': request.data.get('password'),
            }

        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status = status.HTTP_400_BAD_REQUEST)

