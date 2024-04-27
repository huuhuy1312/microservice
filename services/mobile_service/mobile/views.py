from .models import Mobile
from rest_framework import viewsets
from .serializers import MobileSerializer


# Create your views here.
class MobileViewSet(viewsets.ModelViewSet):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer
