from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Boxeador, Luta
from .serializers import BoxeadorSerializer, LutaSerializer

class BoxeadorViewSet(viewsets.ModelViewSet):
    queryset = Boxeador.objects.all()
    serializer_class = BoxeadorSerializer

    @action(methods=['post'], detail=False)
    def realizar_luta(self, request):
        boxeador1 = Boxeador.objects.get(id=request.data['boxeador1'])
        boxeador2 = Boxeador.objects.get(id=request.data['boxeador2'])
        data = request.data['data']
        local = request.data['local']
        vencedor = request.data['vencedor']

        luta = Luta.objects.create(boxeador1=boxeador1, boxeador2=boxeador2, data=data, local=local, vencedor=vencedor)
        luta_serializer = LutaSerializer(luta)

        return Response(luta_serializer.data)

class LutaViewSet(viewsets.ModelViewSet):
    queryset = Luta.objects.all()
    serializer_class = LutaSerializer