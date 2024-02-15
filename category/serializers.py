from rest_framework import serializers
from .models import Subcategory, Category

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'
        verbose_name_plural = "subcategories"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        verbose_name_plural = "categories"