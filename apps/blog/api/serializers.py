from rest_framework import serializers
from apps.blog.models import BlogPost, BlogSidebarImage


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model  = BlogPost
        fields = "__all__"

class BlogSidebarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogSidebarImage
        fields = "__all__"
