from rest_framework import serializers
from .models import Boxeador, Luta

class BoxeadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boxeador
        fields = '_all_'

class LutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Luta
        fields = '_all_'