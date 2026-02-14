from django.db import models
from django.utils.text import slugify

class BlogPost(models.Model):
    title        = models.CharField(max_length=160)
    slug         = models.SlugField(unique=True, blank=True)
    cover_image  = models.ImageField(upload_to="blog/covers/")
    excerpt      = models.CharField(max_length=250, blank=True)
    content      = models.TextField()
    published_at = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ["-published_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:60]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class BlogSidebarImage(models.Model):
    title = models.CharField(max_length=100, blank=True, help_text="Texto Alt para la imagen")
    image = models.ImageField(upload_to="blog/sidebar/", help_text="Imagen para el carrusel lateral")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Imagen Lateral Blog"
        verbose_name_plural = "Imágenes Lateral Blog"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title or f"Imagen {self.id}"
