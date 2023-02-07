from django.urls import path, include
from rest_framework import routers
from .views import LutaViewSet
from .views import BoxeadorViewSet

router = routers.DefaultRouter()
router.register(r'lutas', LutaViewSet, basename='lutas')
router.register(r'boxeadores', BoxeadorViewSet, basename='boxeadores')



urlpatterns = [
    path('', include(router.urls)),
]