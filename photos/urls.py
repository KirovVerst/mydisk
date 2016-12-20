from rest_framework.routers import DefaultRouter
from photos.views import PhotoViewSet

router = DefaultRouter()
router.register(r'^', PhotoViewSet, base_name='photos')

urlpatterns = router.urls
