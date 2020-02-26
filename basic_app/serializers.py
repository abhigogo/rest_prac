from rest_framework import serializers
from basic_app.models import Languages

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Languages
        fields = ('id','name','paradigm')