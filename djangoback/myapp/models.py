from django.db import models
# from django.contrib.gis.db import models as gis_models  # To handle geographic fields like PointField
from django.utils import timezone

class Vehicle(models.Model):
    # Basic vehicle information
    vehicle_id = models.CharField(max_length=100, primary_key=True)
    vehicle_type = models.CharField(max_length=50)  # e.g., Truck, Van, etc.
    license_plate = models.CharField(max_length=20, unique=True)
    manufacturer = models.CharField(max_length=50, null=True, blank=True)
    model = models.CharField(max_length=50, null=True, blank=True)
    year_of_manufacture = models.PositiveIntegerField(null=True, blank=True)

    # Status & operational data
    status = models.CharField(
        max_length=20,
        choices=[('available', 'Available'), ('in_transit', 'In Transit'), ('maintenance', 'Maintenance')],
        default='available'
    )
    fuel_level = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Fuel level in liters or percentage
    mileage = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Total mileage in kilometers

    # Location & tracking
    # current_location = gis_models.PointField(null=True, blank=True)  # Current GPS location
    # destination = gis_models.PointField(null=True, blank=True)  # Destination point
    last_tracked_time = models.DateTimeField(default=timezone.now)

    # Cargo information
    max_load_capacity = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Capacity in kg
    current_load_weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Current load in kg

    # Maintenance and inspection details
    last_service_date = models.DateField(null=True, blank=True)
    next_service_due = models.DateField(null=True, blank=True)
    insurance_expiry = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.vehicle_type} ({self.license_plate})"

    def is_service_due(self):
        """Returns True if the vehicle is due for servicing."""
        if self.next_service_due:
            return timezone.now().date() >= self.next_service_due
        return False



class Shipment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    shipment_id = models.CharField(max_length=100, primary_key=True)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="shipments", null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Shipment {self.shipment_id}"
    

class Event(models.Model):
    EVENT_TYPE_CHOICES = [
        ('pickup', 'Pickup'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('delayed', 'Delayed'),
        ('cancelled', 'Cancelled'),
    ]

    event_id = models.CharField(max_length=100, primary_key=True)
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, related_name="events")
    timestamp = models.DateTimeField(default=timezone.now)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPE_CHOICES)

    def __str__(self):
        return f"Event {self.event_id} for Shipment {self.shipment_id}"