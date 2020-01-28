from django import forms
from .models import Profile, CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['username','first_name','last_name','email']

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        exclude = ['password']
        fields = ['username','first_name','last_name','email']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['password']
        fields = ['age','description','photo']
