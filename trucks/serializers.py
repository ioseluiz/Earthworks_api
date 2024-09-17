from rest_framework import serializers

from .models import Truck

class TruckSerializer(serializers.Serializer):
    code = serializers.CharField()
    model = serializers.CharField()
    brand = serializers.CharField()
    capacity = serializers.FloatField()
    

    def create(self, validated_data):
        return Truck.objects.create(**validated_data)