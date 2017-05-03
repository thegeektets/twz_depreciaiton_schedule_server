from django.db import models

# Create your models here.
import datetime
import hashlib

from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils.translation import ugettext_lazy as _

from depreciation_classes.models import DepreciationClass
from users.models import  User


# Create your models here.
class Asset(models.Model):
    class Meta:
        verbose_name = _('Assets')
        verbose_name_plural = _('Assets')

    title = models.CharField(null=False, blank=False, max_length=255)
    acquisition_cost = models.DecimalField(decimal_places=2, max_digits=1000, default=0)
    acquisition_date = models.DateField(null=False, blank=False)
    depreciation_class = models.ForeignKey('depreciation_classes.DepreciationClass', null=True, blank=True)
    employee_incharge = models.ForeignKey('users.User' , null=False, blank=False)

    serial_number = models.TextField(blank=False, null=False)

    def __str__(self):
        return "%s" % (self.title)