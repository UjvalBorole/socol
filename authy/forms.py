from django import forms
from django.contrib.auth.models  import User
# from user.models  import Profile
from django.contrib.auth.forms import UserCreationForm

class UserRegistration(UserCreationForm):
    first_name = forms.CharField(label='First Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='last Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password(again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True ,widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = [ 'username','email','first_name','last_name','password1','password2']