
from django.db import models
from django.utils.translation import gettext_lazy as _

class StockStatus(models.TextChoices):
    IN_STOCK = 'In stock', _('In stock')
    OUT_OF_STOCK = 'Out of stock', _('Out of stock')
    BACKORDERED = 'Backordered', _('Backordered')