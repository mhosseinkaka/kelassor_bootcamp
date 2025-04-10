from rest_framework.serializers import ModelSerializer
from foreign_villa.models import ForeignVilla

class ForeignVillaSerializer(ModelSerializer):
    class Meta:
        model = ForeignVilla
        fields = '__all__'


class ForeignVillaListSerializer(ModelSerializer):
    class Meta:
        model = ForeignVilla
        fields = ['id', 'title']