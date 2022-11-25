from django import forms
from django.forms import ModelForm
from .models import Product
from crispy_forms.helper import FormHelper


class ProductForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model = Product
        fields = (
            "category",
            "name",
            "price",
        )
        label = {
            "category": '',


        }

        widgets = {
            'category': forms.Select(attrs={'class': 'form-select', 'aria-label': '.form-select'}),
        }
