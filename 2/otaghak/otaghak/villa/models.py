from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    national_id = models.CharField(max_length=11, unique=True)
    email = models.EmailField(null=True, blank=True) #optional
    
    def __str__(self):
        return self.name


class Place(models.Model):
    title = models.CharField(max_length=100)
    address = models.TextField()
    price = models.IntegerField()
    is_valid = models.BooleanField(default=True)
    datetime = models.DateTimeField()
    added_datetime = models.DateTimeField(auto_now_add=True)
    seller = models.ForeignKey(to=Seller, on_delete=models.CASCADE)