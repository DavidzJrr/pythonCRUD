from rest_framework import viewsets
from . import models
from . import serializers

class PerfumeViewset(viewsets.ModelViewSet):
    queryset = models.Perfumes.objects.all()
    serializer_class = serializers.PerfumeSerializer
