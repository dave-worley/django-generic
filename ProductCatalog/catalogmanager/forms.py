from django.forms import ModelForm
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