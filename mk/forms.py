from django import forms
from django.contrib.auth.models import User
from mk.models import Customer
class CustForm(forms.ModelForm): 
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta():
		model = User
		fields = ('username','password')
class CustProfileInfoForm(forms.ModelForm):
	class Meta():
		model = Customer
		fields = ('cust_id','name','dob','pan','mobile','residence')
