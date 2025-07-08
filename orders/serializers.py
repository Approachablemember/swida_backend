from rest_framework import serializers
from .models import Order, Waypoint

class WaypointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waypoint
        fields = ['location', 'waypoint_type']

class OrderSerializer(serializers.ModelSerializer):
    waypoints = WaypointSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'order_number', 'customer_name', 'date', 'waypoints']

    def create(self, validated_data):
        waypoints_data = validated_data.pop('waypoints', [])
        order = Order.objects.create(**validated_data)
        for waypoint_data in waypoints_data:
            Waypoint.objects.create(order=order, **waypoint_data)
        return order
