from rest_framework.serializers import ModelSerializer
from foreign_villa.models import ForeignVilla

class ForeignVillaSerializer(ModelSerializer):
    class Meta:
        model = ForeignVilla
        fields = ['title','price']