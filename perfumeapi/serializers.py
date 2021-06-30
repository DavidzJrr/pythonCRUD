# api <-> mobile app/ web app/ etc. json

from rest_framework import serializers
from .models import Perfumes

class PerfumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfumes
        fields = '__all__'