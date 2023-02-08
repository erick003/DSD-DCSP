from django.urls import path, include
from rest_framework import routers
from .views import LutaViewSet
from .views import BoxeadorViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

class RealizarLutaView(APIView):
    def post(self, request):
        # lógica para realizar luta
        # ...
        return Response({'status': 'luta realizada com sucesso'})

router = routers.DefaultRouter()
router.register(r'lutas', LutaViewSet, basename='lutas')
router.register(r'boxeadores', BoxeadorViewSet, basename='boxeadores')


urlpatterns = [
    path('realizar-luta/', RealizarLutaView.as_view(), name='realizar-luta'),
    path('', include(router.urls)),
]

