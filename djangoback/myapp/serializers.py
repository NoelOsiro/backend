from rest_framework import serializers
from .models import Vehicle, Shipment, Event

class VehicleSerializer(serializers.ModelSerializer):
    is_service_due = serializers.ReadOnlyField()  # Adding a field to indicate if service is due

    class Meta:
        model = Vehicle
        fields = [
            'vehicle_id',
            'vehicle_type',
            'license_plate',
            'manufacturer',
            'model',
            'year_of_manufacture',
            'status',
            'fuel_level',
            'mileage',
            'last_tracked_time',
            'max_load_capacity',
            'current_load_weight',
            'last_service_date',
            'next_service_due',
            'insurance_expiry',
            'is_service_due',
        ]
        read_only_fields = ['is_service_due', 'last_tracked_time']  # Making read-only fields

    def validate_fuel_level(self, value):
        """Validate that fuel level is a positive value."""
        if value < 0:
            raise serializers.ValidationError("Fuel level must be positive.")
        return value

    def validate_mileage(self, value):
        """Validate that mileage is a positive value."""
        if value < 0:
            raise serializers.ValidationError("Mileage must be positive.")
        return value

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = [
            'shipment_id',
            'origin',
            'destination',
            'status',
            'vehicle',
            'created_at'
        ]
        read_only_fields = ['created_at']
        

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'event_id',
            'shipment',
            'timestamp',
            'event_type'
        ]