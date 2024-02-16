from rest_framework import serializers
from .models import Order, OrderItem
from django.core.mail import send_mail
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        exclude=["order"]
        verbose_name_plural = "order Items"
class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = '__all__'
        verbose_name_plural = "orders"
    def create(self, validated_data):
        order_items = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)
        for item in order_items:
            OrderItem.objects.create(order_id=order.id, **item)
        send_mail(
            'Instance {} has been created'.format(order.pk),
            'Here is the message. DATA: {}'.format(validated_data),
            'zhuldyznamazbayeva@gmail.com',
            ['zhuldyznamazbayeva@gmail.com'],
            fail_silently=False,
        )

        return order
