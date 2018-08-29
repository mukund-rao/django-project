# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Customer(models.Model):
	cust_id = models.CharField(max_length=30,primary_key=True,default='')
	name = models.CharField(max_length=30)
	dob = models.DateField()
	pan = models.CharField(max_length=30)
	virt_money = models.FloatField(default=25000)
	#username = models.OneToOneField(User,max_length=30,on_delete=models.CASCADE)	
	mobile = models.CharField(max_length=15)
	residence = models.CharField(max_length=15)
class Broker(models.Model):
	trade_name = models.CharField(max_length=30,primary_key=True)
	bse_no = models.CharField(max_length=30)
	nse_no = models.CharField(max_length=30)
	validity = models.DateField()
	Tax = models.FloatField(default=0.0)
class Stocks(models.Model):
	isin = models.CharField(max_length=30,primary_key=True)
	equity_name = models.CharField(max_length=30)
	prev_close = models.FloatField(default=0.0)
	today_open = models.FloatField(default=0.0)
	today_high = models.FloatField(default=0.0)
	today_low = models.FloatField(default=0.0)	
	current_rate = models.FloatField(default=0.0)
class Transaction(models.Model):
	trans_id = models.CharField(max_length=30,primary_key=True)
	trans_date = models.DateField()
	isin2 = models.ForeignKey('Stocks',on_delete=models.CASCADE)
	buyer_id2 = models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='customer_buyer_id')
	seller_id2 = models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='customer_seller_id')
	buy_avg = models.FloatField(default=0.0)
	quantity = models.IntegerField(default=0)
	buy_value = models.FloatField(default=0.0)
	trans_tax = models.FloatField(default=0.0)
	brokerage = models.FloatField(default=0.0)
class Owns(models.Model):
	cust_id2 = models.ForeignKey('Customer',on_delete=models.CASCADE)
	isin2 = models.ForeignKey('Stocks',on_delete=models.CASCADE)
	quantity = models.IntegerField(default=0)
	buy_rate = models.FloatField(default=0.0)
class Order(models.Model):
	cust_id2 = models.ForeignKey('Customer',on_delete=models.CASCADE,default='')
	isin2 = models.ForeignKey('Stocks',on_delete=models.CASCADE)
	ask_rate = models.FloatField(default=0.0)
	ask_quantity = models.FloatField(default=0.0)
	def get_absolute_url(self):
		return reverse("mk:stock_owned")


