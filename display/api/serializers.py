from rest_framework import serializers

from django.contrib.auth.models import Group, User 
from display.models import Traducao
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class TraducaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Traducao
        fields = ['text', 'language']

        def create(self, validated_data):
            return Traducao.objects.create(**validated_data)

    