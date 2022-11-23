import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Product(models.Model):
    class Category(models.TextChoices):
        CBCT = "01", "CBCT"
        PANO = "02", "Panoramic"
        CEPH = "03", "Cephalomeric"

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.CharField(
        max_length=2,
        choices=Category.choices,
        default='CBCT'
    )
    name = models.CharField(max_length=30, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return self.name
