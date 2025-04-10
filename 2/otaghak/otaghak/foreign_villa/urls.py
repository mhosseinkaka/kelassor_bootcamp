from django.urls import path
from foreign_villa.views import villa_list, VillaListView, VillaRetrieveView, CreateVillaView, DeleteVillaView, UpdateVillaView, CreateListVillaView, RetriveUpdateDeleteVillaView

urlpatterns = [
    path('old-list', villa_list),
    path('list', VillaListView.as_view()),
    path('retrieve/<int:pk>', VillaRetrieveView.as_view()),
    path('create', CreateVillaView.as_view()),
    path('delete/<int:pk>', DeleteVillaView.as_view()),
    path('update/<int:pk>',UpdateVillaView.as_view()),
    path('list-create', CreateListVillaView.as_view()),
    path('retrieve-delete-update/<int:pk>', RetriveUpdateDeleteVillaView.as_view())
]