from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    category_info = serializers.SerializerMethodField()

    def get_category_info(self, obj):
        return {
            'id': obj.category_info.id,
            'name': obj.category_info.name,
            # Include any other fields you want from the Category model
        }
    class Meta:
        model = Product
        fields = '__all__'
        verbose_name_plural = "products"
