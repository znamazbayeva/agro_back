from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('', views.CategoryViewSet, basename='category')
router.register('', views.SubcategoryViewSet, basename='subcategory')

urlpatterns = [] + router.urls