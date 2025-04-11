from rest_framework.serializers import ModelSerializer, StringRelatedField
from foreign_villa.models import ForeignVilla
from villa.models import Seller

class SellerSerializer(ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'

class ForeignVillaSerializer(ModelSerializer):
    # Just for GET
    # creator = StringRelatedField()
    # seller = SellerSerializer()
    class Meta:
        model = ForeignVilla
        fields = '__all__'
        read_only_fields = ['creator']


class ForeignVillaListSerializer(ModelSerializer):
    class Meta:
        model = ForeignVilla
        fields = '__all__'