from django.db import models
import uuid

class Product(models.Model):
    pid = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()
    is_digtial = models.BooleanField()
    created_at = models.DateTimeField()
    is_active = models.BooleanField()

class ProductLine(models.Model):
    price = models.DecimalField(decimal_places=2)
    sku = models.UUIDField(default=uuid.uuid4) #versao suportada pelo db
    stock_qty = models.IntegerField()
    is_active = models.BooleanField()
    weight = models.FloatField()

class productImage(models.Model):
    name = models.CharField(max_length=100)
    alternative_text = models.CharField(max_length=100)
    url = models.ImageField()
    order = models.IntegerField()

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    is_active = models.BooleanField()

class Category(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    name = models.CharField(max_length=100)