# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from mk.models import Customer,Broker,Stocks,Transaction,Owns,Order
# Register your models here.
admin.site.register(Customer)
admin.site.register(Broker)
admin.site.register(Stocks)
admin.site.register(Transaction)
admin.site.register(Owns)
admin.site.register(Order)
