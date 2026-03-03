from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ProjectBannerViewSet

router = DefaultRouter()
router.register("banners", ProjectBannerViewSet, basename="banner-proyecto")
router.register("", ClientViewSet, basename="cliente")
urlpatterns = router.urls
