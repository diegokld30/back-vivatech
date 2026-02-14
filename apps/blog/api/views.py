from rest_framework import viewsets, permissions, filters
from apps.blog.models import BlogPost, BlogSidebarImage
from .serializers import BlogPostSerializer, BlogSidebarImageSerializer

class BlogPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogPost.objects.filter(is_published=True)
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "excerpt", "content"]

    def get_queryset(self):
        queryset = super().get_queryset()
        slug = self.request.query_params.get("slug")
        if slug:
            queryset = queryset.filter(slug=slug)
        return queryset

class BlogSidebarImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogSidebarImage.objects.filter(is_active=True)
    serializer_class = BlogSidebarImageSerializer
    permission_classes = [permissions.AllowAny]
