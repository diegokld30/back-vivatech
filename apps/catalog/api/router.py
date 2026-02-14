from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet

router = DefaultRouter()
#  /api/productos/…  y  /api/categorias/…
router.register("productos", ProductViewSet, basename="producto")
router.register("categorias", CategoryViewSet, basename="categoria")

urlpatterns = router.urls          # <— permitirá include(router)
