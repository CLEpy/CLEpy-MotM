# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.test import TestCase

# Create your tests here.
from .models import Order


class OrderTest(TestCase):
    def test_lawful_return(self):
        order = Order.objects.create(customer="Returny Customer",
                                     address="1 main street",
                                     item="blue lightsaber",
                                     price=100,
                                     is_cancelled=False,
                                     is_shipped=True,
                                     is_returned=True)
        order.cancel()
        self.assertTrue(order.is_cancelled)

    def test_lawful_cancellation(self):
        order = Order.objects.create(customer="Cancelly Customer",
                                     address="1 main street",
                                     item="blue lightsaber",
                                     price=100,
                                     is_cancelled=False,
                                     is_shipped=False,
                                     is_returned=False)
        order.cancel()
        self.assertTrue(order.is_cancelled)

    def test_fraudster(self):
        order = Order.objects.create(customer="Fraudy McFraudstein",
                                     address="1 main street",
                                     item="blue lightsaber",
                                     price=100,
                                     is_cancelled=False,
                                     is_shipped=True,
                                     is_returned=False)
        with self.assertRaises(ValidationError):
            order.cancel()
