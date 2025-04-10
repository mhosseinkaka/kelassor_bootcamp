from django.shortcuts import render
from foreign_villa.models import ForeignVilla
from django.http.response import JsonResponse
from rest_framework.generics import ListAPIView
from foreign_villa.serializers import ForeignVillaSerializer


def villa_list(request):
    villas = ForeignVilla.objects.all().values('title')
    villas = list(villas)
    return JsonResponse(villas,safe=False)
    
# return list of foreign villas
class VillaListView(ListAPIView):
    queryset = ForeignVilla.objects.all()
    serializer_class = ForeignVillaSerializer