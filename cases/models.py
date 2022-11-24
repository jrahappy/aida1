import uuid
from django.db import models
from products.models import Product
from django.contrib.auth import get_user_model
from django.urls import reverse


class Case(models.Model):
    REASON_FOR_SCAN = [
        ('implant', 'Implant'),
        ('sinus', 'Sinus'),
        ('tmj', 'TMJ'),
        ('surgery', 'Surgery'),
        ('others', 'Others'),
    ]
    ROI = [
        ('man', 'Mandible'),
        ('max', 'Maxilla'),
        ('both', 'Both Jaws'),
        ('tmj', 'TMJ'),

    ]

    CASE_STATUS = [
        ('draft',       'Draft'),
        ('arrange',     'In scheduling'),
        ('schedule',    'Schedule confirmed'),
        ('capture',     'Image captured'),
        ('finished',    'Case finished'),
    ]

    author = models.ForeignKey(
        get_user_model(), null=True, on_delete=models.CASCADE)
    reason = models.CharField(
        max_length=50, choices=REASON_FOR_SCAN, default='implant')
    roi = models.CharField(max_length=100, choices=ROI, default='both')
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=10, choices=CASE_STATUS, default='draft')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.reason

    # def get_absolute_url(self):
    #     return reverse('cases:detail', kwargs={'pk': self.pk})


class Patient(models.Model):

    GENDER = [
        ('M', 'Male'),
        ('F', 'Female'),
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
    COUNTRY_CHOICES = [
        ('USA', 'United State'),
        ('CANADA', 'Canada'),
        ('SKOREA', 'South Korea'),
        ('MEXICO', 'Mexico'),
    ]
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE)
    first_name = models.CharField(
        'full name', max_length=30, null=False, blank=False)
    last_name = models.CharField(
        'full name', max_length=20, null=False, blank=False)
    dob = models.DateField()
    gender = models.CharField(choices=GENDER, max_length=2)
    email = models.CharField('email', max_length=50, null=True, blank=True)
    cellphone = models.CharField(
        'cellphone', max_length=50, null=True, blank=True)
    address = models.CharField(
        'address', max_length=100, null=True, blank=True)
    suite = models.CharField('suite', max_length=50, null=True, blank=True)
    city = models.CharField('city', max_length=50, null=True, blank=True)
    state = models.CharField('state', choices=US_STATES,
                             max_length=10, null=True, blank=True)
    zipcode = models.CharField('zipcode', max_length=10, null=True, blank=True)
    country = models.CharField(
        'country', choices=COUNTRY_CHOICES, max_length=30, null=True, blank=True, default='USA')
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class CaseImage(models.Model):
    IMAGE_CATEGORY = [
        ('presc', 'Prescription'),
        ('dicom', 'Dicom files'),
    ]
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    image_category = models.CharField(
        max_length=10, choices=IMAGE_CATEGORY, default='dicom')
    case_image = models.ImageField(
        upload_to='case_image', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


class CaseProvider(models.Model):
    provider = models.ForeignKey(
        get_user_model(), null=False, on_delete=models.CASCADE)


class CaseItems(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100, null=True, blank=True)
    item_price = models.DecimalField(max_digits=4, decimal_places=2)
    item_tax = models.DecimalField(max_digits=4, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
