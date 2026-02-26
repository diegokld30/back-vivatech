from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, ProductCarouselImageViewSet

router = DefaultRouter()
#  /api/productos/…  y  /api/categorias/…
router.register("productos", ProductViewSet, basename="producto")
router.register("categorias", CategoryViewSet, basename="categoria")
router.register("product-carousel-images", ProductCarouselImageViewSet, basename="product-carousel-image")

urlpatterns = router.urls          # <— permitirá include(router)
