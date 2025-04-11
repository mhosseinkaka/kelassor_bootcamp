from foreign_villa.models import ForeignVilla
from django.http.response import JsonResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from foreign_villa.serializers import ForeignVillaSerializer, ForeignVillaListSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly


def villa_list(request):
    villas = ForeignVilla.objects.all().values('title')
    villas = list(villas)
    return JsonResponse(villas,safe=False)


# return list of foreign villas
class VillaListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ForeignVilla.objects.all()
    serializer_class = ForeignVillaListSerializer


class VillaRetrieveView(RetrieveAPIView):
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