from rest_framework import serializers

class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        text = serializers.CharField(max_length=300)
        language = serializers.CharField(max_length=5)
        fields = ['text','language']
