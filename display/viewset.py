# from rest_framework.views import APIView
from rest_framework import  viewsets
from rest_framework.response import Response

from django.contrib.auth.models import Group, User
from display.models import Traducao

from display.api.serializers import GroupSerializer, UserSerializer, TraducaoSerializer
from django_project.services import get_translate
from rest_framework import status


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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Obtém os dados inseridos
        text = serializer.validated_data.get('text')
        language = serializer.validated_data.get('language')
        target_language = serializer.validated_data.get('target_language')
        # Chama a função de tradução
        translated_text = get_translate(text, language, target_language)

        # Retorna o texto traduzido junto com a resposta
        self.perform_create(serializer)
        return Response({'translated_text': translated_text}, status=status.HTTP_201_CREATED)