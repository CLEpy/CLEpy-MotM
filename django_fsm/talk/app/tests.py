# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
from django_fsm import TransitionNotAllowed

from .models import Order


class OrderTest(TestCase):
    def test_lawful_return(self):
        order = Order.objects.create(customer="Returny Customer",
                                     address="1 main street",
                                     item="blue lightsaber",
                                     price=100)
        order.ship()
        order.save()
        self.assertEqual(order.state, "shipped")

        order.receive_return()
        order.save()
        self.assertEqual(order.state, "returned")

    def test_lawful_cancellation(self):
        order = Order.objects.create(customer="Cancelly Customer",
                                     address="1 main street",
                                     item="blue lightsaber",
                                     price=100)
        order.cancel()
        order.save()
        self.assertEqual(order.state, "cancelled")

    def test_fraudster(self):
        order = Order.objects.create(customer="Fraudy McFraudstein",
                                     address="1 main street",
                                     item="blue lightsaber",
                                     price=100)

        order.ship()
        order.save()

        with self.assertRaises(TransitionNotAllowed):
            order.cancel()
