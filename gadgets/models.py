from django.db import models
from distutils.command.upload import upload
from tokenize import blank_re
from unicodedata import category
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
class Manufacturer(models.Model):
    name = models.CharField(max_length= 150)

    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    name = models.CharField(max_length= 150)
    description = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length= 150)
    description = models.TextField()
    price = models.FloatField()
    created_at = models.DateField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name='tags', related_name='products' )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} {self.price} {self.created_at}"




