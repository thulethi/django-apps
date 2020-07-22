from rest_framework import viewsets

from .models import Hero
from .serializers import HeroSerializer


class HeroViewSet(viewsets.ModelViewSet):
    """
    Provide a GET method handler
    """
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer
