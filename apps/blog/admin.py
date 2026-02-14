from django.contrib import admin
from .models import BlogPost, BlogSidebarImage


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "published_at")
    list_filter = ("is_published",)
    search_fields = ("title", "excerpt", "content")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "published_at"

@admin.register(BlogSidebarImage)
class BlogSidebarImageAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "created_at", "preview_image")
    list_filter = ("is_active",)
    
    def preview_image(self, obj):
        if obj.image:
            from django.utils.html import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        return "-"
