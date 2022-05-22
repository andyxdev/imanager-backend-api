from rest_framework import serializers
from.models import Installation,Status

class InstallationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Installation
        fields = '__all__'

    
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        ordering= ('date',)
        model = Status
        fields = '__all__'