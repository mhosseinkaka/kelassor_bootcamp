from django.db import models
from villa.models import Seller


class ForeignVilla(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    country = models.CharField(max_length=100)
    is_valid = models.BooleanField(default=True)
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT)
