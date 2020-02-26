from django.shortcuts import render
from rest_framework import viewsets
from basic_app.models import Languages
from basic_app.serializers import LanguageSerializer

# Create your views here.

class LanguageView(viewsets.ModelViewSet):
    queryset = Languages.objects.all()
    serializer_class = LanguageSerializer

