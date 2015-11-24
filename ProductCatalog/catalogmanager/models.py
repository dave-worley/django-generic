from django.db import models

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
