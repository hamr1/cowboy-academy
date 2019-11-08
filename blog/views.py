from django.shortcuts import render,redirect, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.forms import(
     UserCreationForm, UserChangeForm, PasswordChangeForm)
from blog.forms import ( RegistrationForm, MentorProfileForm, MenteeProfileForm,
    EditMenteeProfile, EditMentorProfile)
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from blog.forms import EditUserProfile
from django.views import View
from blog.models import MentorProfile, MenteeProfile

from blog.models import MenteeProfile

def home(request):
    return render(request, 'blog/account.html')

def RegisterLanding(request):
    return render(request, 'blog/reg_home.html')

def MentorRegister(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        profile_form = MentorProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect(reverse('blog:account'))
        else:
            user_form = RegistrationForm(request.POST)
            profile_form = MentorProfileForm(request.POST)
            args = {'user_form': user_form, 'profile_form': profile_form}
            return render(request, 'blog/mentor_reg_form.html', args)

    else:
        user_form = RegistrationForm()
        profile_form = MentorProfileForm()
        args = {'user_form': user_form, 'profile_form': profile_form}
        return render(request, 'blog/mentor_reg_form.html', args)

def MenteeRegister(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        profile_form = MenteeProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()
            profile = profile_form.save(commit=False)
            profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect(reverse('blog:account'))
        else:
            user_form = RegistrationForm(request.POST)
            profile_form = MenteeProfileForm(request.POST)
            args = {'user_form': user_form, 'profile_form': profile_form}
            return render(request, 'blog/mentee_reg_form.html', args)

    else:
        user_form = RegistrationForm()
        profile_form = MenteeProfileForm()
        args = {'user_form': user_form, 'profile_form': profile_form}
        return render(request, 'blog/mentee_reg_form.html', args)

def view_profile(request):
    args= {'user': request.user}
    return render(request, 'blog/profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('blog:view_profile'))
        else:
            return redirect(reverse('blog:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)
        args={'form': form}
        return render(request, 'blog/change_password.html', args)


#This is working for Mentees 
#Need to add in Mentor possibility               
def edit_profile(request):
    if request.user.is_mentee:
        if request.method == 'POST':
            user_form = EditUserProfile(request.POST, instance=request.user, prefix="user")
            profile_form = EditMenteeProfile(request.POST, instance=request.user.menteeprofile)            
            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                return redirect(reverse('blog:view_profile'))
        else:
            user_form = EditUserProfile(instance=request.user, prefix="user")
            profile_form = EditMenteeProfile(instance=request.user.menteeprofile)
        args = {'user_form': user_form, 'profile_form': profile_form}
        return render(request,'blog/edit_profile.html', args)
    elif request.user.is_mentor:
        if request.method == 'POST':
            user_form = EditUserProfile(request.POST, instance=request.user, prefix="user")
            profile_form = EditMentorProfile(request.POST, instance=request.user.mentorprofile)            
            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                return redirect(reverse('blog:view_profile'))
        else:
            user_form = EditUserProfile(instance=request.user, prefix="user")
            profile_form = EditMentorProfile(instance=request.user.mentorprofile)

        args = {'user_form': user_form, 'profile_form': profile_form}
        return render(request,'blog/edit_profile.html', args)

                    