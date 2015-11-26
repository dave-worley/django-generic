from django.forms import ModelForm
from django.forms import ValidationError
from django import forms
import geocoder
from .models import Product, Order


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


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = (
            'recipient_name',
            'address',
            'city',
            'state',
            'zip',
            'phone',
            'quantity',
        )

    def clean(self):
        super().clean()
        # check the address
        g = geocoder.google('{} {}, {} {}'.format(
            self.cleaned_data['address'],
            self.cleaned_data['city'],
            self.cleaned_data['state'],
            self.cleaned_data['zip']
        ))
        if g.housenumber and g.postal == self.cleaned_data['zip']:
            return self.cleaned_data
        else:
            raise ValidationError('Please use a valid US address.')