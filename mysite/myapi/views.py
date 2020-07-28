from .models import Hero
from .serializers import HeroSerializer
from rest_framework import viewsets, generics


class HeroListCreateAPIView(generics.ListCreateAPIView):
    """
    API view to retrieve list of heroes or create a new one
    """
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class HeroDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete a hero
    """
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
