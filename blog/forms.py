from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.utils import timezone
from blog.models import UserProfile


class RegistrationForm(UserCreationForm):

    email = forms.EmailField(required=True)
    #Define any new fields (carreer interest, city, state, etc) Here
    #Remember to name them in meta

    class Meta:
        model  = User
        fields = {
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        }
        def save(self, commit=True):
            user = super(self, RegistrationForm).save(commit=False)
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']

            if commit:
                user.save()
    field_order =['username','first_name','last_name', 'email','password1','password2' ]
    
class EditProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        #Toggle which fields to include from Profile Edit
        fields = (
            'email',
            'first_name',
            'last_name'
        )
        #Toggle which fields to exclude from Profile Edit
        exclude = ()
    field_order =['first_name','last_name','email']


##Attempt at Protile Form
class EditUserProfile(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields = (
            'description',
            'city',
            'state',
            'website',
            'phone',
            'career_interest'
            
        )