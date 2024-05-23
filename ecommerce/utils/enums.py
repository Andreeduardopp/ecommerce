
from django.db import models
from django.utils.translation import gettext_lazy as _

class StockStatus(models.TextChoices):
    IN_STOCK = 'In stock', _('In stock')
    OUT_OF_STOCK = 'Investimento', _('Investimento')
    BACKORDERED = 'Backordered', _('Backordered')