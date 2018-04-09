# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.db import models


class Order(models.Model):
    customer = models.CharField(max_length=255)
    address = models.CharField(max_length=1000)
    item = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)

    # Customers should be able to cancel their order, duh!
    is_cancelled = models.BooleanField(default=False)

    # We've been taken for $100k in cancellation fraud, oops
    is_shipped = models.BooleanField(default=False)
    is_returned = models.BooleanField(default=False)

    def refund(self):
        # return the money
        pass

    def cancel(self):
        if not self.is_shipped or self.is_returned:
            self.refund()
            self.is_cancelled = True
            self.save()
        else:
            raise ValidationError("FRAUD! ABORT!")
