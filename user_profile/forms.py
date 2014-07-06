from django import forms
from django.contrib.auth.models import User
from user_profile.models import *

class UserForm(forms.ModelForm):
	first_name = forms.charField()
	last_name = forms.charField()
	phone_number = forms.IntegerField()
	password = forms.charField(widget=forms.PasswordInput())
	
	class Meta:
		model = User
		fields = ('username', 'email', 'password')
		
class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('profile_pic','phone_number')

class ProfilePicChangeForm(forms.Form):
	picture = forms.ImageField(label='your new profile pic')
	
