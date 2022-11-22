from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class CustomUser(AbstractUser):

    WORKING_DEPARTMENT = [
        ('SALES', 'Sales'),
        ('MARKE', 'Marketing'),
        ('ACCOU', 'Accounting'),
        ('MANUF', 'Manufacturing'),
        ('PLANN', 'Planning'),
    ]
    phone = models.CharField('Phone', max_length=20, null=True, blank=True)
    department = models.CharField(
        max_length=5, choices=WORKING_DEPARTMENT, default='SALES', null=True, blank=True)
    sales_area = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'CustomUser'

    def get_absolute_url(self):
        return reverse('yprofile:your_profile', args=[str(self.id)])
