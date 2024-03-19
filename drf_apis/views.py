from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Dictionary

class BookViewSet(viewsets.ModelViewSet):
    queryset = Dictionary.objects.all()
    serializer_class = BookSerializer
