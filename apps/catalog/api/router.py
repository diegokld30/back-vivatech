from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
#  /api/productos/…  (lista)   y  /api/productos/{id}/ (detalle)
router.register("", ProductViewSet, basename="producto")

urlpatterns = router.urls          # <— permitirá include(router)
