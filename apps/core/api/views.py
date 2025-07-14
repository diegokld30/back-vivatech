from rest_framework import viewsets, permissions
from apps.core.models import FAQ
from .serializers import FAQSerializer

class FAQViewSet(viewsets.ReadOnlyModelViewSet):
    queryset           = FAQ.objects.filter(is_active=True)
    serializer_class   = FAQSerializer
    permission_classes = [permissions.AllowAny]
