from django.contrib import admin
from .models import Product, ProductImage, Category, ProductCarouselImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


from django.db import models
from ckeditor.widgets import CKEditorWidget
from django_json_widget.widgets import JSONEditorWidget

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ("name", "category", "price", "is_active", "created_at")
    list_filter = ("is_active",)
    search_fields = ("name", "short_desc", "description")
    prepopulated_fields = {"slug": ("name",)}
    
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
        models.JSONField: {'widget': JSONEditorWidget},
    }


@admin.register(ProductCarouselImage)
class ProductCarouselImageAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "order")
    list_editable = ("is_active", "order")
    list_filter = ("is_active",)
