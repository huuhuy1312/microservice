from rest_framework.routers import DefaultRouter
from .views import SearchEngineViewSet

router = DefaultRouter()
router.register(r'', SearchEngineViewSet, basename="search-engine")

urlpatterns = router.urls