from django import forms
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

class UserEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('picture', 'full_name','bio','website','phone_number','gender','is_private_account')
        labels = {
            'is_private_account':'Do You want to make Your Account Private',
            'phone_number':'Phone',
            'email' :'Email',
            'bio':'Bio',
            'picture':'Profile Pic',
            'gender':'Gender',
            'website':'Website'
        }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs) #it gives the fields list which is given in the form

        for field in self.fields:
            if field == "picture":
                self.fields[field].widget.attrs.update({'class':'form-control-file'})
            elif field == 'is_private_account':
                self.fields[field].widget.attrs.update({'class':'form-check-input'})
            else:
                self.fields[field].widget.attrs.update({'class':'form-control form-control-sm'})

