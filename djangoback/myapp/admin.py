"""_summary_
    Admin module for customizing the Django admin interface for the Vehicle and Shipment models.
    Classes:
        VehicleAdmin: Customizes the admin interface for the Vehicle model.
        ShipmentAdmin: Customizes the admin interface for the Shipment model.

    Returns:
        _type_: _description_
    """
from django.contrib import admin
from .models import Vehicle, Shipment, Event  # Ensure Shipment is defined in models.py


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    """
    VehicleAdmin class for customizing the Django admin interface for the Vehicle model.
    Attributes:
        list_display (tuple): Fields to display in the list view.
        list_filter (tuple): Fields to filter by in the admin interface.
        search_fields (tuple): Fields to search by in the admin interface.
        readonly_fields (tuple): Fields that are read-only in the admin interface.
    Methods:s
        is_service_due(obj):
            Display if the vehicle is due for service.
    """

    list_display = (
        'vehicle_id',
        'vehicle_type',
        'license_plate',
        'status',
        'last_tracked_time',
        'next_service_due',
        'is_service_due'
    )
    # Fields to filter by
    list_filter = ('status', 'vehicle_type', 'next_service_due')
    # Fields to search by
    search_fields = ('vehicle_id', 'license_plate', 'manufacturer', 'model')
    # Read-only fields
    readonly_fields = ('last_tracked_time', 'is_service_due')

    def is_service_due(self, obj):
        """Display if the vehicle is due for service."""
        return obj.is_service_due()
    is_service_due.boolean = True


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    """
    Admin interface options for the Shipment model.
    This class customizes the Django admin interface for the Shipment model,
    providing specific configurations for list display, filtering, searching,
    and read-only fields.
    Attributes:
        list_display (tuple): Fields to display in the list view.
        list_filter (tuple): Fields to filter by in the admin interface.
        search_fields (tuple): Fields to search by in the admin interface.
        readonly_fields (tuple): Fields that are read-only in the admin interface.
    """
    # Fields to display in the list view
    list_display = ('shipment_id', 'origin', 'destination',
                    'status', 'vehicle', 'created_at')
    # Fields to filter by
    list_filter = ('status', 'created_at')
    # Fields to search by
    search_fields = ('shipment_id', 'origin', 'destination')
    # Read-only fields
    readonly_fields = ('created_at',)
    
@admin.register(Event)

class EventAdmin(admin.ModelAdmin):
    """
    Admin interface options for the Event model.
    This class customizes the Django admin interface for the Event model,
    providing specific configurations for list display, filtering, searching,
    and read-only fields.
    Attributes:
        list_display (tuple): Fields to display in the list view.
        list_filter (tuple): Fields to filter by in the admin interface.
        search_fields (tuple): Fields to search by in the admin interface.
        readonly_fields (tuple): Fields that are read-only in the admin interface.
    """
    # Fields to display in the list view
    list_display = ('event_id', 'shipment', 'timestamp', 'event_type')
    # Fields to filter by
    list_filter = ('event_type', 'timestamp')
    # Fields to search by
    search_fields = ('event_id', 'shipment')
    # Read-only fields
    readonly_fields = ('timestamp',)
