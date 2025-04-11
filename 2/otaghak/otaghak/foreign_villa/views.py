from foreign_villa.models import ForeignVilla
from django.http.response import JsonResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from foreign_villa.serializers import ForeignVillaSerializer, ForeignVillaListSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny
from foreign_villa.permissions import IsAlireza
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


def villa_list(request):
    villas = ForeignVilla.objects.all().values('title')
    villas = list(villas)
    return JsonResponse(villas,safe=False)


# return list of foreign villas
class VillaListView(ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = ForeignVilla.objects.all()
    serializer_class = ForeignVillaListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['seller','creator']
    search_fields = ['title']
    ordering_fields = ['price']


class VillaRetrieveView(RetrieveAPIView):
    permission_classes = [IsAlireza]
    queryset = ForeignVilla.objects.all()
    serializer_class = ForeignVillaSerializer


class CreateVillaView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ForeignVilla.objects.all()
    serializer_class = ForeignVillaSerializer
    
    def perform_create(self, serializer):
        serializer.save(
            creator = self.request.user 
        )


class DeleteVillaView(DestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = ForeignVilla.objects.all()
    serializer_class = ForeignVillaSerializer


class UpdateVillaView(UpdateAPIView):
    queryset = ForeignVilla.objects.all()
    serializer_class = ForeignVillaSerializer


class CreateListVillaView(ListCreateAPIView):
    queryset = ForeignVilla.objects.all()
    serializer_class = ForeignVillaSerializer


class RetriveUpdateDeleteVillaView(RetrieveUpdateDestroyAPIView):
    queryset = ForeignVilla.objects.all()
    serializer_class = ForeignVillaSerializer