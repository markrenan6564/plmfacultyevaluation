from django.contrib.auth.forms import BaseUserCreationForm
from django import forms

from django.conf import settings
from django.contrib.auth import get_user_model



class AccountLoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'border-2/[1px] border-gray-200 text-black sm:w-full w-8/12', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'border-2/[1px] border-gray-200 text-black sm:w-full w-8/12', 'placeholder': 'Password'}))
    

class AccountCreationForm(BaseUserCreationForm):
    pass
