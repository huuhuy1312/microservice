from .models import Clothes
from rest_framework import viewsets
from .serializers import ClothesSerializer


# Create your views here.
class ClothesViewSet(viewsets.ModelViewSet):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer
