from rest_framework import serializers
from apps.about.models import AboutSection, AboutStat, AboutGalleryImage


class AboutStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutStat
        fields = ["id", "label", "value", "icon", "order"]


class AboutGalleryImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.url) if obj.image else None

    class Meta:
        model = AboutGalleryImage
        fields = ["id", "image", "alt", "order"]


class AboutSectionSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    stats = AboutStatSerializer(many=True, read_only=True)
    gallery_images = AboutGalleryImageSerializer(many=True, read_only=True)

    def get_image(self, obj):
        if not obj.image:
            return None
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.url)

    class Meta:
        model = AboutSection
        fields = [
            "id", "section_type", "title", "subtitle", "body",
            "image", "background_color", "order", "is_active",
            "stats", "gallery_images",
        ]
