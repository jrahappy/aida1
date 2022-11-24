from django import forms
from django.forms import ModelForm
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = (
            "category",
            "name",
            "price",
        )
        widgets = {
            'category': forms.Select(attrs={'class': 'form-select', 'aria-label': '.form-select'}),
        }
