from django.urls import path, include
# from rest_framework import routers

from . views import HeroListCreateAPIView, HeroDetailsAPIView

# router = routers.DefaultRouter()
# router.register(r'heroes', views.HeroViewSet)

# Wipe up API using automatic URL routing. Additionally, we include login URLs for browsable API
# app_name = 'api'
urlpatterns = [
    # path('', include(router.urls)),
    path('heroes/', HeroListCreateAPIView.as_view(), name='heroes'),
    path('heroes/<int:pk>/', HeroDetailsAPIView.as_view(), name='hero-details'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
