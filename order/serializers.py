from rest_framework import serializers
from .models import Order, OrderItem
from product.models import Product
from product.serializers import ProductSerializer
from django.core.mail import EmailMessage
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
        order_string = ""
        for item in order_items:
            OrderItem.objects.create(order_id=order.id, **item)
            product_data = Product.objects.get(id=item['product'].id)
            order_string += "Продукт: {} Количеcтво: {} Цена: {} \n".format(product_data.name, item['quantity'], product_data.price)
        order_string += "Имя: {}, Телефон: {}".format(validated_data["name"], validated_data["phone"])
        email = EmailMessage(
            'Заказ #{}'.format(order.pk),
            order_string,
            to=['askar.agroweb@gmail.com'],
        )
        email.send()

        return order
