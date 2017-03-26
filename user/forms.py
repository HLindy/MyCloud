from user.models import User
from django import forms
class adduserform(forms.Form):
    class Meta:
        model=User
        fields=['username','password','name','phonenumber','email','organizationname','role']