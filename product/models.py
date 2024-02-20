from django.db import models
from category.models import Category, Subcategory
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True) 
    discounted_price = models.IntegerField(null=True, blank=True) 
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    manifacturor = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    add_info = models.CharField(max_length=500, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    count = models.IntegerField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
