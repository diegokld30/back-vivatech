from rest_framework import viewsets, permissions, filters
from apps.catalog.models import Product, Category, ProductCarouselImage
from .serializers import ProductSerializer, CategorySerializer, ProductCarouselImageSerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset           = Category.objects.all()
    serializer_class   = CategorySerializer
    permission_classes = [permissions.AllowAny]


class ProductViewSet(viewsets.ModelViewSet):
    queryset           = Product.objects.filter(is_active=True)
    serializer_class   = ProductSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends    = [filters.SearchFilter, filters.OrderingFilter]
    search_fields      = ["name", "short_desc", "description", "category__name"]
    ordering_fields    = ["created_at", "price"]

    def get_queryset(self):
        qs = super().get_queryset()
        category_slug = self.request.query_params.get("category", None)
        product_slug = self.request.query_params.get("slug", None)
        if category_slug:
            qs = qs.filter(category__slug=category_slug)
        if product_slug:
            qs = qs.filter(slug=product_slug)
        return qs


class ProductCarouselImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductCarouselImage.objects.filter(is_active=True)
    serializer_class = ProductCarouselImageSerializer
    permission_classes = [permissions.AllowAny]
