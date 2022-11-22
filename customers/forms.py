from django import forms
from django.forms import ModelForm
from .models import Customer, Person


class CustomerForm(ModelForm):

    class Meta:
        model = Customer
        fields = (
            "business",
            "address",
            "suite",
            "city",
            "state",
            "zipcode",
            "country",
            "website",
            "contact_name",
            "description",
        )
        labels = {
            "business": 'Business name',
            "address": 'Address',
            "suite": 'Suite',
            "city": 'City',
            "state": 'State',
            "zipcode": 'Zip code',
            "country": 'Country',
            "website": 'Website',
            "contact_name": 'Contact name',
            "description": 'Description',
        }
        COUNTRY_CHOICES = [

        ]

        widgets = {
            'country': forms.Select(attrs={'class': 'form-select', 'aria-label': '.form-select'}),
            'state': forms.Select(attrs={'class': 'form-select', 'aria-label': '.form-select'}),
        }


class PersonForm(ModelForm):

    class Meta:
        model = Person

        fields = (
            "full_name",
            "email",
            "cellphone",
            "office_phone",
            "description",
            "is_deleted",
        )

        labels = {
            "full_name": 'Full name',
            "email": 'Email',
            "cellphone": 'Cell phone',
            "office_phone": 'Office phone',
            "description": 'Description',
        }
        # widgets = {
        #     "salutation":  forms.Select(choices=SALUTATION_CHOICES, attrs={'class': 'form-select', 'aria-label': '.form-select'}),
        # }
