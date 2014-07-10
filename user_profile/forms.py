from django import forms
from django.contrib.auth.models import User
from user_profile.models import *
from passwords.fields import PasswordField

class UserForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput())
    #confirm_password = forms.CharField(widget=forms.PasswordInput())

    password = PasswordField(label="Password")
    confirm_password = PasswordField(label="Confirm Password")
	
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['email'].label = 'Email'
        #self.fields['password'].required = False
        #self.fields['confirm_password'].required = False
    
    def clean(self):
        if 'password' in self.cleaned_data and 'confirm_password' in self.cleaned_data:
            password1 = self.cleaned_data['password']
            password2 = self.cleaned_data['confirm_password']
            if password1 != password2:
                msg = "Your passwords didn't match."
                #self.add_error('password', msg)
                #self.add_error('confirm_password', msg)
                raise forms.ValidationError("Your passwords did not match.")
        return self.cleaned_data

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
	
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic','phone_number')

class ProfilePicChangeForm(forms.Form):
    picture = forms.ImageField(label='your new profile pic')

