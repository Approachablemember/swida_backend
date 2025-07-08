from django.urls import path
from .views import OrderCreateAPIView, OrderListAPIView

urlpatterns = [
    path('orders/create/', OrderCreateAPIView.as_view(), name='order-create'),
    path('orders/', OrderListAPIView.as_view(), name='order-list'),
]
