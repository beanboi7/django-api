# Create your views here.

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import AddAdvisor
from .serializers import AdvisorSerializer

class AdvisorView(APIView):

    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'photo': request.data.get('photo'),
        }

        serializer = AdvisorSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_200_OK)
        
        return Response(status = status.HTTP_400_BAD_REQUEST)