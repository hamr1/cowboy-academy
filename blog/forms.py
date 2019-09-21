from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    #Define any new fields (carreer interest, city, state, etc) Here
    #Remember to name them in meta
    career_interest = forms.CharField(max_length=40, label='career_interest')

    class Meta:
        model  = User
        fields = {
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'career_interest'
        }
        def save(self, commit=True):
            user = super(RegistrationForm, self).save(commit=False)
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']
            user.career_interest =self.cleaned_data['career_interest']

            if commit:
                user.save()
    field_order =['username','first_name','last_name','career_interest','email','password1','password2' ]

    
class EditProfileForm(UserChangeForm):
    
    class Meta:
        model = User
        #Toggle which fields to include from Profile Edit
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )
        #Toggle which fields to exclude from Profile Edit
        exclude = ()
    field_order =['first_name','last_name','email']
