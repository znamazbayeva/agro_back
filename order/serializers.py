from rest_framework import serializers
from .models import Order, OrderItem
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
        verbose_name_plural = "order Items"
class OrderSerializer(serializers.ModelSerializer):
    products = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = '__all__'
        verbose_name_plural = "orders"
    def create(self, validated_data):
        products = validated_data.pop('products')
        order = Order.objects.create(**validated_data)
        for track_data in products:
            Order.objects.create(order=order, **track_data)
        return order
