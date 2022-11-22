import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Customer(models.Model):

    COUNTRY_CHOICES = [
        ('USA', 'United State'),
        ('CANADA', 'Canada'),
        ('SKOREA', 'South Korea'),
        ('MEXICO', 'Mexico'),
    ]

    US_STATES = [
        ("AK", "Alaska"),
        ("AL", "Alabama"),
        ("AR", "Arkansas"),
        ("AS", "American Samoa"),
        ("AZ", "Arizona"),
        ("CA", "California"),
        ("CO", "Colorado"),
        ("CT", "Connecticut"),
        ("DC", "District of Columbia"),
        ("DE", "Delaware"),
        ("FL", "Florida"),
        ("GA", "Georgia"),
        ("GU", "Guam"),
        ("HI", "Hawaii"),
        ("IA", "Iowa"),
        ("ID", "Idaho"),
        ("IL", "Illinois"),
        ("IN", "Indiana"),
        ("KS", "Kansas"),
        ("KY", "Kentucky"),
        ("LA", "Louisiana"),
        ("MA", "Massachusetts"),
        ("MD", "Maryland"),
        ("ME", "Maine"),
        ("MI", "Michigan"),
        ("MN", "Minnesota"),
        ("MO", "Missouri"),
        ("MS", "Mississippi"),
        ("MT", "Montana"),
        ("NC", "North Carolina"),
        ("ND", "North Dakota"),
        ("NE", "Nebraska"),
        ("NH", "New Hampshire"),
        ("NJ", "New Jersey"),
        ("NM", "New Mexico"),
        ("NV", "Nevada"),
        ("NY", "New York"),
        ("OH", "Ohio"),
        ("OK", "Oklahoma"),
        ("OR", "Oregon"),
        ("PA", "Pennsylvania"),
        ("PR", "Puerto Rico"),
        ("RI", "Rhode Island"),
        ("SC", "South Carolina"),
        ("SD", "South Dakota"),
        ("TN", "Tennessee"),
        ("TX", "Texas"),
        ("UT", "Utah"),
        ("VA", "Virginia"),
        ("VI", "Virgin Islands"),
        ("VT", "Vermont"),
        ("WA", "Washington"),
        ("WI", "Wisconsin"),
        ("WV", "West Virginia"),
        ("WY", "Wyoming"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(
        get_user_model(), null=True, on_delete=models.SET_NULL)
    business = models.CharField(
        'business', max_length=50, null=False, blank=False)
    address = models.CharField(
        'address', max_length=100, null=True, blank=True)
    suite = models.CharField('suite', max_length=50, null=True, blank=True)
    city = models.CharField('city', max_length=50, null=True, blank=True)
    state = models.CharField('state', choices=US_STATES,
                             max_length=10, null=True, blank=True)
    zipcode = models.CharField('zipcode', max_length=10, null=True, blank=True)
    country = models.CharField(
        'country', choices=COUNTRY_CHOICES, max_length=30, null=True, blank=True, default='USA')
    website = models.CharField('website', max_length=50, null=True, blank=True)
    contact_name = models.CharField(
        'contact name', max_length=50, null=True, blank=True)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    salesrep = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.business

    def get_absolute_url(self):
        return reverse('customers:detail', kwargs={'pk': self.pk})


class Person(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    full_name = models.CharField(
        'full name', max_length=50, null=False, blank=False)
    photo = models.ImageField(upload_to='person_photos', null=True, blank=True)
    email = models.CharField('email', max_length=50, null=True, blank=True)
    cellphone = models.CharField(
        'cellphone', max_length=50, null=True, blank=True)
    office_phone = models.CharField(
        'office phone', max_length=50, null=True, blank=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
