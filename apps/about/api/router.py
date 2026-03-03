from rest_framework.routers import DefaultRouter
from .views import AboutSectionViewSet

router = DefaultRouter()
router.register("", AboutSectionViewSet, basename="about-section")
urlpatterns = router.urls
