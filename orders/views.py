from rest_framework import generics, filters
from .models import Order
from .serializers import OrderSerializer
from django_filters.rest_framework import DjangoFilterBackend

class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['customer_name', 'date', 'order_number']
    ordering_fields = ['order_number', 'customer_name', 'date']
    ordering = ['order_number']
