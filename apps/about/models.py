from django.db import models


class AboutSection(models.Model):
    """Sección editable de la página Sobre Nosotros."""

    SECTION_TYPES = [
        ("hero", "Hero / Banner principal"),
        ("text", "Texto con imagen"),
        ("stats", "Estadísticas / Cifras"),
        ("gallery", "Galería de imágenes"),
        ("cta", "Llamado a la acción"),
    ]

    section_type = models.CharField(
        "Tipo de sección",
        max_length=20,
        choices=SECTION_TYPES,
        default="text",
    )
    title = models.CharField("Título", max_length=200)
    subtitle = models.CharField("Subtítulo", max_length=300, blank=True)
    body = models.TextField(
        "Contenido (HTML)",
        blank=True,
        help_text="Contenido enriquecido de la sección (acepta HTML).",
    )
    image = models.ImageField(
        "Imagen",
        upload_to="about/sections/",
        blank=True,
        null=True,
        help_text="Imagen principal de la sección.",
    )
    background_color = models.CharField(
        "Color de fondo",
        max_length=30,
        blank=True,
        help_text="Ej: #e3f2e5, transparent, primary. Dejarlo vacío usa el tema.",
    )
    order = models.PositiveIntegerField("Orden", default=0)
    is_active = models.BooleanField("Activo", default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "sección"
        verbose_name_plural = "secciones"

    def __str__(self):
        return f"[{self.get_section_type_display()}] {self.title}"


class AboutStat(models.Model):
    """Cifra/estadística dentro de una sección tipo stats."""

    section = models.ForeignKey(
        AboutSection,
        on_delete=models.CASCADE,
        related_name="stats",
        limit_choices_to={"section_type": "stats"},
    )
    label = models.CharField("Etiqueta", max_length=80)
    value = models.CharField(
        "Valor",
        max_length=40,
        help_text="Ej: 150+, 18, 5.300",
    )
    ICON_CHOICES = [
        ("", "— Sin icono —"),
        ("tractor", "🚜 Tractor / Maquinaria"),
        ("users", "👥 Personas / Clientes"),
        ("map-pin", "📍 Ubicación / Ciudades"),
        ("award", "🏆 Premio / Logro"),
        ("leaf", "🌿 Agricultura / Sostenibilidad"),
        ("wrench", "🔧 Servicio técnico"),
        ("shield-check", "✅ Garantía / Seguridad"),
        ("heart", "❤️ Satisfacción"),
        ("star", "⭐ Calidad / Destacado"),
        ("zap", "⚡ Tecnología / Energía"),
        ("globe", "🌍 Cobertura / Global"),
        ("truck", "🚛 Entregas / Logística"),
    ]

    icon = models.CharField(
        "Icono",
        max_length=60,
        blank=True,
        choices=ICON_CHOICES,
        default="leaf",
    )
    order = models.PositiveIntegerField("Orden", default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "estadística"
        verbose_name_plural = "estadísticas"

    def __str__(self):
        return f"{self.label}: {self.value}"


class AboutGalleryImage(models.Model):
    """Imagen dentro de una sección tipo gallery."""

    section = models.ForeignKey(
        AboutSection,
        on_delete=models.CASCADE,
        related_name="gallery_images",
        limit_choices_to={"section_type": "gallery"},
    )
    image = models.ImageField("Imagen", upload_to="about/gallery/")
    alt = models.CharField("Texto alternativo", max_length=120, blank=True)
    order = models.PositiveIntegerField("Orden", default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "imagen de galería"
        verbose_name_plural = "imágenes de galería"

    def __str__(self):
        return self.alt or f"Imagen {self.id}"
