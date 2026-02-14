from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet, BlogSidebarImageViewSet

router = DefaultRouter()
router.register("posts", BlogPostViewSet, basename="post")
router.register("sidebar-images", BlogSidebarImageViewSet, basename="sidebar-image")

urlpatterns = router.urls
