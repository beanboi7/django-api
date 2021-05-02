from .models import AddUser
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddUser
        fields = ('name','email','password')

