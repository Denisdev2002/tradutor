# from rest_framework.views import APIView
from rest_framework import  viewsets
from rest_framework.response import Response

from display.models import Traducao

from display.api.serializers import  TraducaoSerializer
from django_project.services import get_translate
from rest_framework import status

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

        print(translated_text)
        return Response({'translated_text': translated_text}, status=status.HTTP_201_CREATED)




    