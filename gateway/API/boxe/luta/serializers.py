from rest_framework import serializers
from .models import Boxeador, Luta

class BoxeadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boxeador
        fields = '__all__'

class LutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Luta
        fields = '__all__'