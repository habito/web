from django import forms
from django.contrib.auth.models import User
from user_profile.models import *

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['email'].label = 'Email'

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic','phone_number')

class ProfilePicChangeForm(forms.Form):
    picture = forms.ImageField(label='your new profile pic')

