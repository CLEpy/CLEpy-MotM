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

    state = FSMField(default="ordered")

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
        if self.state in ('cancelled', 'returned'):
            return 0
        else:
            return self.price
