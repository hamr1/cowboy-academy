from django import forms
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.utils import timezone
from blog.models import MentorProfile, User, MenteeProfile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model  = User
        fields = {
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'city',
            'state',
            'phone',
            'is_mentor',
            'is_mentee'
        }
        def save(self, commit=True):
            user = super(self, RegistrationForm).save(commit=False)
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']
            user.city = self.cleaned_data['city']
            user.state = self.cleaned_data['state']
            user.phone = self.cleaned_data['phone']
            
            if commit:
                user.save()
            return user
    field_order =['username','first_name','last_name', 'email', 'city', 'state', 'phone','password1','password2']

class MenteeProfileForm(forms.ModelForm): #I don't think UserCreation Form Is Right here
    #Define any new fields (carreer interest, city, state, etc) Here
    #Remember to name them in meta
    class Meta:
        model  = MenteeProfile
        fields = {
            'career_interest1',
            'career_interest2',
            'career_interest3'
        }
        def save(self, commit=True):
            user = super(self, RegistrationForm).save(commit=False)
            user.career_interest1 = self.cleaned_data['career_interest1']
            user.career_interest2 = self.cleaned_data['career_interest2']
            user.career_interest3 = self.cleaned_data['career_interest3']

            if commit:
                user.save()
            return MenteeProfile
    field_order =('career_interest1', 'career_interest2', 'career_interest3')

#Attempt at Protile Form
class EditUserProfile(forms.ModelForm):
    
    class Meta:
        model=User
        fields = (
            'first_name',
            'last_name',
            'description',
            'city',
            'state',
            'website',
            'phone',
            'email',
            #'image'
        )


class EditMenteeProfile(forms.ModelForm):
    class Meta:
        model= MenteeProfile
        fields = (
        'career_interest1',
        'career_interest2',
        'career_interest3'
        )
        field_order =('career_interest1', 'career_interest2', 'career_interest3')


class EditMentorProfile(forms.ModelForm):
    class Meta:
        model=MentorProfile
        fields = (
        'career_expertise1',
        'career_expertise2',
        'career_expertise3',
        'career_expertise4',
        'career_expertise5',
        'career_expertise6',
        )

class MentorProfileForm(forms.ModelForm):
    #Define any new fields (carreer interest, city, state, etc) Here
    #Remember to name them in meta
    class Meta:
         model = MentorProfile
         fields = {
             'career_expertise1',
             'career_expertise2',
             'career_expertise3',
             'career_expertise4',
             'career_expertise5',
             'career_expertise6',
            #  'mentor_capacity'
         }
         def save(self, commit=True):
             user = super(self, MentorRegistrationForm).save(commit=False)
             user.career_expertise1 = self.cleaned_data['career_expertise1']
             user.career_expertise2 = self.cleaned_data['career_expertise2']
             user.career_expertise3 = self.cleaned_data['career_expertise3']
             user.career_expertise4 = self.cleaned_data['career_expertise4']
             user.career_expertise5 = self.cleaned_data['career_expertise5']
             user.career_expertise6 = self.cleaned_data['career_expertise6']
           
             if commit:
                 user.save()
             return user
    field_order =['mentor_capacity','career_expertise1','career_expertise2','career_expertise3', 'career_expertise4', 
    'career_expertise5', 'career_expertise6']
