from rest_framework import serializers

from .models import Hero
from .models import Translation

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'alias')

class TranslationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Translation
        fields = ('origin_text', 'target_text', 'unique')
