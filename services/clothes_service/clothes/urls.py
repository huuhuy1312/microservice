from rest_framework.routers import DefaultRouter
from .views import ClothesViewSet

router = DefaultRouter()
router.register(r"clothes", ClothesViewSet)

urlpatterns = router.urls
