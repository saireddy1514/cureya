from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms import TextInput, EmailInput
from django.forms.widgets import Select
from .models import *
class RegistrationData(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input','placeholder': 'Password'}), required=True)
	class Meta:
		model= Registration
		fields=('name','gender','email','phoneno','password')
		widgets={
		'name':forms.TextInput(attrs={'class':'input','placeholder':'Name'}),
		'gender':forms.Select(attrs={'class':'input','placeholder':'Gender'}),
		'email':forms.EmailInput(attrs={'class':'input','placeholder':'Email'}),
		'phoneno':forms.TextInput(attrs={'class':'input','placeholder':'Phone No'}),

		}

class DoctorRegistrationData(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input','placeholder': 'Password'}), required=True)
	class Meta:
		model= DoctorRegistration
		fields=('name','gender','email','phoneno','experience','workfield','address','password')
		widgets={
		'name':forms.TextInput(attrs={'class':'input','placeholder':'Name'}),
		'gender':forms.Select(attrs={'class':'input','placeholder':'Gender'}),
		'email':forms.EmailInput(attrs={'class':'input','placeholder':'Email'}),
		'phoneno':forms.TextInput(attrs={'class':'input','placeholder':'Phone No'}),
		'experience':forms.TextInput(attrs={'class':'input','placeholder':'Experience(Years)'}),
		'workfield':forms.TextInput(attrs={'class':'input','placeholder':'WorkField'}),
		'address':forms.TextInput(attrs={'class':'input','placeholder':'Address'}),
		}