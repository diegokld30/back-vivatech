from rest_framework import viewsets, permissions
from apps.about.models import AboutSection
from .serializers import AboutSectionSerializer


class AboutSectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutSection.objects.filter(is_active=True).prefetch_related(
        "stats", "gallery_images"
    )
    serializer_class = AboutSectionSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_context(self):
        return {"request": self.request}
