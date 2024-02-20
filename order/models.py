from django.db import models
from product.models import Product

# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name="Имя")
    phone = models.CharField(max_length=200, null=True, blank=True, verbose_name="Телефон")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
class OrderItem(models.Model):
    order=models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE,default=None, verbose_name="Заказ")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
    quantity = models.IntegerField(default=1, verbose_name="Количество")