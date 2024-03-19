from rest_framework import serializers
from .models import Dictionary

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dictionary
        fields = '__all__'