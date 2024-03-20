from django.shortcuts import render

# Create your views here.
# from django.views.generic import TemplateView
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .api.serializers import TranslationSerializer
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
class TranslationAPIView(APIView):
    serializer_class = TranslationSerializer
    
    def obter_traducao(request):
        serializer = TranslationSerializer(data=request.data)
        try:
            if request.method == 'POST':
                text = serializer.validated_data.get('text')
                language = serializer.validated_data.get('language')
                return Response({'text': text, 'language': language}, status=201)
        except serializer.DoesNotExist:
            return Response(serializer.errors, status=400)


