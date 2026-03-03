from django.contrib import admin
from .models import Client, ClientImage, ProjectBanner


class ClientImageInline(admin.TabularInline):
    model = ClientImage
    extra = 1


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display  = ("name", "location", "is_active", "created_at")
    list_filter   = ("is_active",)
    search_fields = ("name", "location", "testimonial", "content")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ClientImageInline]
    fieldsets = (
        ("Información básica", {
            "fields": ("name", "slug", "logo", "cover", "location"),
        }),
        ("Contenido", {
            "fields": ("testimonial", "content"),
            "description": "Resumen corto y contenido HTML enriquecido del proyecto.",
        }),
        ("Video", {
            "fields": ("video_url",),
            "description": "URL de YouTube, TikTok u otra plataforma para embeber video.",
        }),
        ("Ubicación GPS", {
            "fields": ("latitude", "longitude"),
            "classes": ("collapse",),
        }),
        ("Estado", {
            "fields": ("is_active",),
        }),
    )


@admin.register(ProjectBanner)
class ProjectBannerAdmin(admin.ModelAdmin):
    list_display  = ("title", "is_active", "order", "created_at")
    list_filter   = ("is_active",)
    list_editable = ("order", "is_active")
    search_fields = ("title", "description")
    fieldsets = (
        (None, {
            "fields": ("title", "description"),
        }),
        ("Medios", {
            "fields": ("image", "video_url"),
            "description": "Imagen y/o video del banner. Si ambos existen, el video tiene prioridad.",
        }),
        ("Configuración", {
            "fields": ("is_active", "order"),
        }),
    )
