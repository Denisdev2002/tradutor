# from rest_framework.views import APIView
from rest_framework import  viewsets
from rest_framework.decorators import api_view
# from rest_framework.response import Response

from django.contrib.auth.models import Group, User
from display.models import Traducao

from display.api.serializers import GroupSerializer, UserSerializer, TraducaoSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer

class TraducaoViewSet(viewsets.ModelViewSet):
    queryset = Traducao.objects.all()
    serializer_class = TraducaoSerializer
