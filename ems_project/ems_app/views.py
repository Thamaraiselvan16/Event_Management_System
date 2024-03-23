from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.
from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.decorators import  api_view, permission_classes
from rest_framework import status

@api_view(['GET','POST'])
def details(request, format=None):
    if request.method=='GET':
        details=Event.objects.all()
        userdata=Events(details,many=True)
        return Response(userdata.data)
    
from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from datetime import datetime, timedelta
from geopy.distance import geodesic

@api_view(['GET'])
def find_events(request):
    if request.method == 'GET':
        try:
            latitude = float(request.GET.get('latitude'))
            longitude = float(request.GET.get('longitude'))
            date_str = request.GET.get('date')
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
        except (ValueError, TypeError):
            return Response({"error": "Invalid latitude, longitude, or date format"}, status=status.HTTP_400_BAD_REQUEST)

        # Query events occurring within the next 14 days from the specified date
        end_date = date + timedelta(days=14)
        events = Event.objects.filter(date__range=[date, end_date]).order_by('date')[:10]

        event_data = []
        for event in events:
            # Calculate distance from user's location
            event_location = (event.latitude, event.longitude)
            user_location = (latitude, longitude)
            distance = geodesic(user_location, event_location).kilometers

            # Serialize event data
            event_serializer = Events(event)
            serialized_event = event_serializer.data

            # Add distance to serialized event data
            serialized_event['distance'] = distance

            event_data.append(serialized_event)

        return Response(event_data)



# http://localhost:8000/events/find/?latitude=40.7128&longitude=-74.0060&date=2024-03-22