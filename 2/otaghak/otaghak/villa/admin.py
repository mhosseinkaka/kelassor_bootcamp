from django.contrib.admin import ModelAdmin, register
from villa.models import Seller, Place


@register(Seller)
class SellerAdmin(ModelAdmin):
    list_display = ['name', 'phone']
    search_fields = ['national_id']


@register(Place)
class PlaceAdmin(ModelAdmin):
    list_display = ['title', 'price', 'is_valid']
    search_fields = ['title', 'address']
    ist_filter = ["is_valid"]
    autocomplete_fields = ['seller']
