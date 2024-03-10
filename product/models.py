from django.db import models
from category.models import Category, Subcategory
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name="Название")
    price = models.IntegerField(null=True, blank=True, verbose_name="Розничная цена") 
    discounted_price = models.IntegerField(null=True, blank=True, verbose_name="Оптовая цена") 
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name="Субкатегория")
    manifacturor = models.CharField(max_length=200, null=True, blank=True, verbose_name="Производитель")
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name="Краткое описание")
    add_info = models.TextField(max_length=500, null=True, blank=True, verbose_name="Полное описание")
    photo = models.ImageField(null=True, blank=True, verbose_name="Фото")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    count = models.IntegerField(verbose_name="Количество")
    @property
    def category_info(self):
        return self.subcategory.category
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
