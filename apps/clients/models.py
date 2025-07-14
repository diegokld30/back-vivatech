# apps/clients/models.py
from django.db import models
from django.utils.text import slugify

class Client(models.Model):
    name        = models.CharField(max_length=120)
    slug        = models.SlugField(unique=True, blank=True)
    logo        = models.ImageField(upload_to="clients/logos/", blank=True)
    cover = models.ImageField(
        upload_to="clients/covers/",
        blank=True,
        null=True,
    )
    testimonial = models.TextField()
    location    = models.CharField(max_length=120, blank=True)
    latitude    = models.DecimalField(max_digits=18, decimal_places=15, null=True, blank=True)
    longitude   = models.DecimalField(max_digits=18, decimal_places=15, null=True, blank=True)
    is_active   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "cliente"
        verbose_name_plural = "clientes"

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
        verbose_name = "imagen de cliente"
        verbose_name_plural = "imagenes de clientes"

    def __str__(self):
        return f"{self.client.name} – {self.id}"
