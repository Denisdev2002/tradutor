from rest_framework import serializers

from display.models import Traducao
from rest_framework import serializers

class TraducaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Traducao
        fields = ['text', 'language','target_language']


    