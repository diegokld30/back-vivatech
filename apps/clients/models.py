# apps/clients/models.py
from django.db import models
from django.utils.text import slugify


class Client(models.Model):
    """Modelo reutilizado para 'Proyectos' (antes Clientes)."""
    name        = models.CharField("Nombre", max_length=120)
    slug        = models.SlugField(unique=True, blank=True)
    logo        = models.ImageField(upload_to="clients/logos/", blank=True)
    cover       = models.ImageField(
        upload_to="clients/covers/",
        blank=True,
        null=True,
    )
    testimonial = models.TextField("Resumen corto", blank=True)
    content     = models.TextField(
        "Contenido (HTML)",
        blank=True,
        help_text="Contenido enriquecido del proyecto (acepta HTML).",
    )
    video_url   = models.URLField(
        "URL de video",
        blank=True,
        null=True,
        help_text="URL de YouTube, TikTok u otra plataforma de video.",
    )
    location    = models.CharField(max_length=120, blank=True)
    latitude    = models.DecimalField(max_digits=18, decimal_places=15, null=True, blank=True)
    longitude   = models.DecimalField(max_digits=18, decimal_places=15, null=True, blank=True)
    is_active   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)[:60]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ClientImage(models.Model):
    client = models.ForeignKey(Client, related_name="gallery", on_delete=models.CASCADE)
    image  = models.ImageField(upload_to="clients/gallery/")
    alt    = models.CharField(max_length=120, blank=True)

    class Meta:
        verbose_name = "imagen de proyecto"
        verbose_name_plural = "imágenes de proyectos"

    def __str__(self):
        return f"{self.client.name} – {self.id}"


class ProjectBanner(models.Model):
    """Banner/highlight que aparece en la parte superior de Lomas Planas."""
    title       = models.CharField("Título", max_length=200)
    description = models.TextField("Descripción", blank=True)
    image       = models.ImageField(
        upload_to="projects/banners/",
        blank=True,
        null=True,
        help_text="Imagen principal del banner.",
    )
    video_url   = models.URLField(
        "URL de video",
        blank=True,
        null=True,
        help_text="URL de YouTube, TikTok u otra plataforma de video.",
    )
    is_active   = models.BooleanField(default=True)
    order       = models.PositiveIntegerField("Orden", default=0)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "-created_at"]
        verbose_name = "banner de proyecto"
        verbose_name_plural = "banners de proyectos"

    def __str__(self):
        return self.title
