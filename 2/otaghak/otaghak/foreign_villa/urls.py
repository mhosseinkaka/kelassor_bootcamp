from django.urls import path
from foreign_villa.views import villa_list, VillaListView

urlpatterns = [
    path('list', villa_list),
    path('new-list', VillaListView.as_view())
]