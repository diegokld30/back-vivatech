from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)[:50]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    # ───── Datos principales ─────
    category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    name        = models.CharField(max_length=120)
    slug        = models.SlugField(unique=True, blank=True)
    cover = models.ImageField(
        upload_to="products/cover/",
        blank=True,
        null=True,
    )

    short_desc  = models.CharField(max_length=160, blank=True)
    description = models.TextField()

    price       = models.DecimalField(max_digits=12, decimal_places=2)
    data_sheet  = models.FileField(                # PDF o ficha técnica
        upload_to="products/datasheets/",
        blank=True,
    )
    video_url   = models.URLField(blank=True, null=True, help_text="URL de YouTube, Vimeo o TikTok")
    specifications = models.JSONField(default=dict, blank=True, help_text="Especificaciones técnicas (clave-valor)")
    hide_price  = models.BooleanField(default=False, verbose_name="Ocultar precio")

    # ───── Control ─────
    is_active   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "producto"
        verbose_name_plural = "productos"

    def save(self, *args, **kwargs):
        # autogenera slug la primera vez
        if not self.slug:
            self.slug = slugify(self.name)[:60]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    """
    Imágenes adicionales (galería) asociadas a cada producto.
    """
    product = models.ForeignKey(
        Product,
        related_name="gallery",
        on_delete=models.CASCADE,
    )
    image   = models.ImageField(upload_to="products/gallery/")
    alt     = models.CharField("texto alternativo", max_length=120, blank=True)

    class Meta:
        verbose_name = "imagen de producto"
        verbose_name_plural = "galería de producto"

    def __str__(self):
        return f"{self.product.name} – #{self.id}"


class ProductCarouselImage(models.Model):
    """
    Imágenes para el slider principal de la sección de productos.
    """
    title = models.CharField(max_length=120, blank=True)
    image = models.ImageField(upload_to="products/carousel/")
    link = models.URLField(blank=True, null=True, help_text="Enlace opcional al hacer clic")
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "imagen carrusel productos"
        verbose_name_plural = "imágenes carrusel productos"

    def __str__(self):
        return self.title or f"Imagen #{self.id}"
