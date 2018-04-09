# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.db import models
from django_fsm import FSMField, transition

BLACKLIST = ["Abusive Returner"]


class Order(models.Model):
    customer = models.CharField(max_length=255)
    address = models.CharField(max_length=1000)
    item = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)

    STATE_CHOICES = (("ordered", "Ordered", "Order"),
                     ("shipped", "Shipped", "Order"),
                     ("returned", "Returned", "CancelledOrder"),
                     ("cancelled", "Cancelled", "CancelledOrder"))
    state = FSMField(default="ordered", state_choices=STATE_CHOICES)

    def refund(self):
        # return the money
        pass

    @transition(field=state, source="ordered", target="shipped")
    def ship(self):
        # send notification email
        pass

    def not_too_expensive_for_return(self):
        return self.price <= 200

    @transition(field=state, source="shipped", target="returned", conditions=[not_too_expensive_for_return],
                permission=lambda instance, user: user not in BLACKLIST)
    def receive_return(self):
        self.refund()

    @transition(field=state, source="ordered", target="cancelled")
    def cancel(self):
        self.refund()

    @property
    def revenue(self):
        return self.price


class CancelledOrder(Order):
    class Meta:
        proxy = True

    @property
    def revenue(self):
        return 0
