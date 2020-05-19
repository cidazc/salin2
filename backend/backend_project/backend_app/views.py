from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import HeroSerializer
from .serializers import TranslationSerializer

from .models import Hero
from .models import Translation

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer
    
class TranslationViewSet(viewsets.ModelViewSet):
    queryset = Translation.objects.all().order_by('origin_text')
    serializer_class = TranslationSerializer
