from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
class StockStatus(models.TextChoices):
    IN_STOCK = 'In stock', _('In stock')
    OUT_OF_STOCK = 'Out of stock', _('Out of stock')
    BACKORDERED = 'Backordered', _('Backordered')
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=False)
    parent_category = models.ForeignKey('self', null=True, on_delete=models.PROTECT)
    #se a categoria tem um pai então ela n]ao pode ser excluida
class SeasonalEvents(models.Model):
    id = models.BigAutoField(primary_key=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    name = models.CharField(max_length=100, unique=True)

class ProductType(models.Model):
    name = models.CharField( max_length=100)
    parent = models.ForeignKey("self", on_delete=models.CASCADE)
class Product(models.Model):
    pid = models.CharField(max_length=255)
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True) 
    seasonal_events = models.ForeignKey(SeasonalEvents, on_delete=models.SET_NULL, null=True)
    description = models.TextField(blank=True, null=True)
    is_digtial = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    is_active = models.BooleanField(default=False)
    stock_status = models.CharField(max_length=13, choices=StockStatus.choices, default=StockStatus.OUT_OF_STOCK)
    #podemos adicionar um dic tbm nas choices
    product_type = models.ManyToManyField(ProductType,through="Product_ProductType", related_name="product_type")

class Attribute(models.Model): #para que a productLine não precise carregar todos os attr de um produto
    name = models.CharField( max_length=100)
    description = models.TextField(null=True)
class AttributeValue(models.Model):
    attribute_value=models.CharField(max_length=100)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
class ProductLine(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=5)
    sku = models.UUIDField(default=uuid.uuid4) #versao suportada pelo db
    product = models.ForeignKey(Product, on_delete=models.PROTECT) #todas as product line devem ser excluidas antes de um produto
    stock_qty = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    order = models.IntegerField()
    weight = models.FloatField()
    attribute_values = models.ManyToManyField(AttributeValue,through="ProductLine_AttributeValue", related_name="attibute")
class productImage(models.Model):
    name = models.CharField(max_length=100)
    product_line = models.ForeignKey(ProductLine, on_delete=models.CASCADE)
    alternative_text = models.CharField(max_length=100)
    url = models.ImageField()
    order = models.IntegerField()

class ProductLine_AttributeValue(models.Model):
    attribute_value =models.ForeignKey(AttributeValue, on_delete=models.CASCADE)
    product_line = models.ForeignKey(ProductLine, on_delete=models.CASCADE)

class Product_ProductType(models.Model):
    product =models.ForeignKey(Product, on_delete=models.CASCADE)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)

class StockControl(models.Model):
    stock_qty = models.IntegerField()
    name = models.CharField(max_length=50)
    stock_product = models.OneToOneField(Product, on_delete=models.CASCADE)