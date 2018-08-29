# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView

# Create your views here.

from mk.forms import CustForm,CustProfileInfoForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import models
from mk.models import Customer,Broker,Stocks,Transaction,Owns,Order

def index(request):
	return render(request,'mk/index.html')

@login_required
def index2(request):
	user=str(request.user.username)
	profile=Customer.objects.get(cust_id=user)
	str1 = ""+profile.cust_id
	str2 = ""+profile.name
	str3 = ""+str(profile.dob)
	str4 = ""+profile.mobile
	str5 = ""+profile.residence
	profile_dict={'cust_id':str1,'name':str2,'dob':str3,'mobile':str4,'residence':str5}
	return render(request,'mk/index2.html',context=profile_dict)

@login_required
def stock_owned(request):
	user=str(request.user.username)
	stow=Owns.objects.filter(cust_id2=user)
	print(stow)
	stow_dict={'stow':stow}
	print(stow_dict)
	return render(request,'mk/stock_owned.html',context=stow_dict)

@login_required
def profile(request):
	user=str(request.user.username)
	profile=Customer.objects.get(cust_id=user)
	str1 = ""+profile.cust_id
	str2 = ""+profile.name
	str3 = ""+str(profile.dob)
	str4 = ""+profile.mobile
	str5 = ""+profile.residence
	profile_dict={'cust_id':str1,'name':str2,'dob':str3,'mobile':str4,'residence':str5}
	return render(request,'mk/profile.html',context=profile_dict)

def order(request):
	user=str(request.user.username)
	ordr=Order.objects.filter(cust_id2=user)
	ordr_dict={'ordr':ordr}
	return render(request,'mk/order.html',context=ordr_dict)

class OrderDetail(DetailView):
	context_object_name='order_detail'
	model=models.Order
	fields=('ask_rate','ask_quantity')


class CreateOrder(CreateView):
	model=models.Order
	fields=('cust_id2','isin2','ask_rate','ask_quantity')

class UpdateOrder(UpdateView):
	model=models.Order
	fields=('ask_rate','ask_quantity')

class DeleteOrder(DeleteView):
	model=models.Order
	success_url = reverse_lazy("mk:order")

def info(request):
	if request.method=="POST":
		info_form = CustProfileInfoForm(data=request.POST)
		if info_form.is_valid():
			inf=info_form.save(commit=True)
			inf.save()
			return HttpResponseRedirect(reverse('index'))
		else:
			return HttpResponse(info_form.errors)
	else:
		info_form=CustProfileInfoForm()
	return render(request,'mk/info.html',{'form2':info_form})



def signUp(request):
	if request.method=="POST":
		user_form = CustForm(data=request.POST)
		if user_form.is_valid():
			user = user_form.save(commit=True)
			user.set_password(user.password)
			user.save()
			return HttpResponseRedirect(reverse('info'))
		else:
			return HttpResponse(user_form.errors)
	else:
		user_form = CustForm()
	return render(request,'mk/signUp.html',{'form1':user_form})




@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))



def user_login(request):
	if request.method=='POST':
		username = request.POST.get('username')
		name=username
		password = request.POST.get('password')
		user = authenticate(username=username,password=password)
		if user:
			if user.is_active:	
				login(request,user)
				return HttpResponseRedirect(reverse('index2'))
			else:
				return HttpResponse("ACCOUNT NOT ACTIVE")
				
		else:
			print("Login failed")
			print("Username : {} and password {}".format(username,password))
			return HttpResponse("Invalid login details")
	else:
		return render(request,'mk/user_login.html',{})
