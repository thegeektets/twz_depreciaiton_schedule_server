from django.db import models

# Create your models here.
import datetime
import hashlib

from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class DepreciationClass(models.Model):
    class Meta:
        verbose_name = _('Depreciation Class')
        verbose_name_plural = _('Depreciation Classes')

    title = models.CharField(null=False, blank=False, max_length=255)
    rate = models.DecimalField(decimal_places=2, max_digits=1000, default=0)

    def __str__(self):
        return "%s" % (self.title)