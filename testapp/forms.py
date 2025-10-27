from django import forms
from .models import UserSignupModel, UserDetails

class UserSignupForm(forms.ModelForm):
    class Meta:
        model = UserSignupModel
        fields = "__all__"
        widgets = {
            "password": forms.PasswordInput(),
        }

class userDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = "__all__"
