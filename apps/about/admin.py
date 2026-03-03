from django.contrib import admin
from .models import AboutSection, AboutStat, AboutGalleryImage


class AboutStatInline(admin.TabularInline):
    model = AboutStat
    extra = 1


class AboutGalleryImageInline(admin.TabularInline):
    model = AboutGalleryImage
    extra = 1


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "section_type", "order", "is_active", "created_at")
    list_filter = ("section_type", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("title", "subtitle", "body")
    inlines = [AboutStatInline, AboutGalleryImageInline]
    fieldsets = (
        (None, {
            "fields": ("section_type", "title", "subtitle"),
            "description": (
                "<b>Tipos de sección:</b><br>"
                "• <b>Hero</b>: Banner grande de entrada (imagen + título grande).<br>"
                "• <b>Texto con imagen</b>: Texto al lado de una imagen (se alternan).<br>"
                "• <b>Estadísticas</b>: Cifras animadas con iconos. Agrega las cifras abajo en 'Estadísticas'.<br>"
                "• <b>Galería</b>: Cuadrícula de fotos. Agrega las fotos abajo en 'Imágenes de galería'.<br>"
                "• <b>CTA</b>: Botón final de contacto con WhatsApp."
            ),
        }),
        ("Contenido", {
            "fields": ("body", "image"),
            "description": (
                "El <b>Contenido (HTML)</b> es opcional. Para el Hero basta con título + subtítulo + imagen.<br>"
                "Si escribes HTML, usa etiquetas simples: &lt;p&gt;, &lt;strong&gt;, &lt;ul&gt;, &lt;li&gt;.<br>"
                "No necesitas estilos inline, el sitio aplica los estilos automáticamente."
            ),
        }),
        ("Apariencia", {
            "fields": ("background_color",),
            "classes": ("collapse",),
        }),
        ("Configuración", {
            "fields": ("order", "is_active"),
        }),
    )
