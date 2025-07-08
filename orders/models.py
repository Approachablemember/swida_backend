from django.db import models

class Order(models.Model):
    order_number = models.IntegerField(max_length=50)
    customer_name = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"{self.order_number} - {self.customer_name}"

class Waypoint(models.Model):
    PICKUP = 'PU'
    DELIVERY = 'DL'
    WAYPOINT_TYPES = [
        (PICKUP, 'Pickup'),
        (DELIVERY, 'Delivery'),
    ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='waypoints')
    location = models.CharField(max_length=255)
    waypoint_type = models.CharField(max_length=2, choices=WAYPOINT_TYPES)

    def __str__(self):
        return f"{self.location} ({self.get_waypoint_type_display()})"
