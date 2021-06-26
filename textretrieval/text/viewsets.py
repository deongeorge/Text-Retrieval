from rest_framework import viewsets
from . import models
from . import serializers

class TextViewset(viewsets.ModelViewSet):
    queryset = models.Text.objects.all()
    serializer_class = serializers.TextSerializer

