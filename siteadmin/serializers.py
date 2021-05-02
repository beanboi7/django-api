from .models import AddAdvisor
from rest_framework import serializers

class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddAdvisor
        fields = ('name','photo')
