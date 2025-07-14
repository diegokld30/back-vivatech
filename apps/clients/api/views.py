from rest_framework import viewsets, permissions
from apps.clients.models import Client
from .serializers import ClientSerializer

class ClientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset           = Client.objects.filter(is_active=True)
    serializer_class   = ClientSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_context(self):
        return {"request": self.request}
