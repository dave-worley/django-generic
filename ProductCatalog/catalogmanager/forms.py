from django.forms import ModelForm
from django import forms
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = (
            'name',
            'description',
            'width',
            'length',
            'height',
            'weight',
            'value',
        )

class ProductsUploadForm(forms.Form):
    file = forms.FileField()