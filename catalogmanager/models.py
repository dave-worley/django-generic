from django.db import models
from localflavor.us.models import USStateField, USZipCodeField, PhoneNumberField

class Product(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    width = models.FloatField()
    length = models.FloatField()
    height = models.FloatField()
    weight = models.FloatField()
    value = models.DecimalField(max_digits=20, decimal_places=2)

    def __unicode__(self):
        return self.name

class Order(models.Model):
    recipient_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = USStateField()
    zip = USZipCodeField()
    phone = PhoneNumberField()

    product = models.ForeignKey(Product)
    quantity = models.IntegerField()

    @property
    def total(self):
        return self.quantity * self.product.value

    def __unicode__(self):
        return "{} ordered by {}".format(self.product.name, self.recipient_name)