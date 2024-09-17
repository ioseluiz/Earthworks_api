from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Truck
from .serializers import TruckSerializer

@api_view(['GET', 'POST'])
def truck_list(request):
    if request.method == 'GET':
        trucks = Truck.objects.all()
        serializer = TruckSerializer(trucks, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = TruckSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
@api_view(['GET'])
def truck_details(request, pk):
    truck = Truck.objects.get(pk=pk)
    serializer = TruckSerializer(truck)
    return Response(serializer.data)
