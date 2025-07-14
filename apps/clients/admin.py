from django.contrib import admin
from .models import Client, ClientImage


class ClientImageInline(admin.TabularInline):
    model = ClientImage
    extra = 1


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display  = ("name", "location", "is_active", "created_at")
    list_filter   = ("is_active",)
    search_fields = ("name", "location", "testimonial")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ClientImageInline]
