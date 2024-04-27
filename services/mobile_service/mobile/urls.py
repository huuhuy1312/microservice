from rest_framework.routers import DefaultRouter
from .views import MobileViewSet

router = DefaultRouter()
router.register(r'mobiles', MobileViewSet)

urlpatterns = router.urls