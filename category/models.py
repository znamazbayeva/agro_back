from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    category_icon = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Subcategory(models.Model):
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    icon = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Субкатегория'
        verbose_name_plural = 'Субкатегории'