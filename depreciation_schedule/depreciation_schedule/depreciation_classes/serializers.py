from rest_framework import serializers
from .models import DepreciationClass

class DepreciationClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = DepreciationClass




