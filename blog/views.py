from django.shortcuts import render,redirect, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.forms import(
     UserCreationForm, UserChangeForm, PasswordChangeForm)
from blog.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def home(request):
    return render(request, 'blog/home.html')

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('blog:login'))
    else:
        form = RegistrationForm()

        args={'form':form}
        return render(request, 'blog/reg_form.html', args)


def view_profile(request):
    args= {'user': request.user}
    return render(request, 'blog/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('blog:view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args={'form': form}
        return render(request, 'blog/edit_profile.html', args)

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