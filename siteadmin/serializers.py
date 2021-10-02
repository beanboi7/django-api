from rest_framework import serializers

from .models import AddAdvisor


class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddAdvisor
        fields = ("name", "photo")
