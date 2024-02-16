from django.shortcuts import render
from .serializers import ProductSerializer
from .models import Product
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
from rest_framework.pagination import PageNumberPagination
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

class ProductViewSet(viewsets.ModelViewSet):
    """
    ---
    parameters:
    - name: subcategory
      in: query
      description: Subcategory filter
      required: false
      type: string
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'subcategory_id', openapi.IN_QUERY, description='Subcategory filter', type=openapi.TYPE_INTEGER
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    def get_queryset(self):
        queryset = super().get_queryset()
        subcategory_id = self.request.query_params.get('subcategory_id')
        if subcategory_id is not None:
            queryset = queryset.filter(subcategory_id=subcategory_id)
        return queryset