from rest_framework import serializers
from apps.blog.models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model  = BlogPost
        fields = "__all__"
