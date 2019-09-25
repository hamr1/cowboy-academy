from django.views.generic import TemplateView
from django.shortcuts import render, redirect

from home.forms import HomeForm


class HomeView(TemplateView):
    template_name='home/home.html'  

    def get(self,request):
        form = HomeForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
            form = HomeForm()
        
        args = {'form':form, 'text':text}
        return render(request, self.template_name, args)


##
def update_profile(request):
    if request.method =='POST':
        user_form =UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance = request.user)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully changed'))
            return redirect('blog:profile')
        else:
            message.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance = request.user)