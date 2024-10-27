"""
    This module defines viewsets for the Vehicle and Shipment models.
Classes:
    VehicleViewSet: A viewset for viewing and editing vehicle instances.
    ShipmentViewSet: A viewset for viewing and editing shipment instances.
    VehicleViewSet.queryset (QuerySet): The queryset that retrieves all Vehicle objects.
    VehicleViewSet.serializer_class (Serializer): The serializer class used to validate and serialize Vehicle objects.
    ShipmentViewSet.queryset (QuerySet): The queryset that retrieves all Shipment objects.
    ShipmentViewSet.serializer_class (Serializer): The serializer class used to validate and serialize Shipment objects.
    ShipmentViewSet.lookup_field (str): The field used to look up a shipment instance. Defaults to 'shipment_id'.
    """
from rest_framework import viewsets

from .models import Vehicle, Shipment
from .serializers import VehicleSerializer, ShipmentSerializer, EventSerializer, Event
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data.update({'email': self.user.email})
        return data

class LoginView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = CustomTokenObtainPairSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        username = email  # Using email as username

        if User.objects.filter(email=email).exists():
            return Response({'error': 'User with this email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)

class VehicleViewSet(viewsets.ModelViewSet):
    """_summary_

    Args:
        viewsets (_type_): _description_
    """
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
# Create your views here.

class ShipmentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing shipment instances.
    Attributes:
        queryset (QuerySet): The queryset that retrieves all Shipment objects.
       serializer_class (Serializer): The serializer class used 
       to validate and serialize Shipment objects.
       lookup_field (str): The field used to look up 
       a shipment instance. Defaults to 'shipment_id'.
    """
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    lookup_field = 'shipment_id'  # Use shipment_id instead of the default pk


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'event_id' 
