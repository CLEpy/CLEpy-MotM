# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models
from django_fsm import FSMField, transition


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

    @transition(field=state, source="shipped", target="returned")
    def receive_return(self):
        self.refund()

    @transition(field=state, source="ordered", target="cancelled")
    def cancel(self):
        self.refund()
