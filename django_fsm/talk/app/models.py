# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Order(models.Model):
    customer = models.CharField(max_length=255)
    address = models.CharField(max_length=1000)
    item = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)
