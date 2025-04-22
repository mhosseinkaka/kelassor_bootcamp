from django.db.models.signals import post_save
from django.dispatch import receiver
from foreign_villa.models import ForeignVilla

@receiver(post_save, sender=ForeignVilla)
def send_new_villa_to_users(sender, instance, created, **kwargs):
    if created:
        ...