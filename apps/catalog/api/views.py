from rest_framework import viewsets, permissions, filters
from apps.catalog.models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset           = Product.objects.filter(is_active=True)
    serializer_class   = ProductSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends    = [filters.SearchFilter, filters.OrderingFilter]
    search_fields      = ["name", "short_desc", "description"]
    ordering_fields    = ["created_at", "price"]
