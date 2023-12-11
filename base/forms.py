from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
    

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2'] 
   
class EnquiryForm(forms.ModelForm):
    class Meta:
        model=models.Enquiry
        fields=['name','email','phone','note']

class VisaForm(forms.ModelForm):
    class Meta:
        model=models.Visa
        exclude=["id"]


class TourCategoryForm(forms.ModelForm):

    class Meta:
        model=models.TourCategory
        exclude=["id"]