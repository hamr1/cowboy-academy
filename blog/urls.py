from django.contrib.auth.views import(
LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, 
PasswordResetConfirmView, PasswordResetCompleteView)
from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import logout
from django.urls import reverse_lazy


app_name = "users"
urlpatterns =[
    path('', LoginView.as_view(template_name='blog/login.html'), name="login"),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name="login"),
    path('account/', LoginView.as_view(template_name='blog/account.html'), name="account"),
    path('account/login/', LoginView.as_view(template_name='blog/login.html'), name="login"),
    path("logout/", LogoutView.as_view(template_name='blog/logout.html'), name="logout"),
    path('account/logout/', LogoutView.as_view(template_name='blog/logout.html'), name="logout"),
    path('register/mentor', views.MentorRegister, name ='mentor_register'),
    path('register/mentee', views.MenteeRegister, name ='mentee_register'),
    path('register/', views.RegisterLanding, name='register'),
    
    path('profile/', views.view_profile, name ='view_profile'),
    path('account/profile/', views.view_profile, name ='view_profile'),

    path('account/profile/<int:pk>/', views.view_profile, name ='view_profile_pk'),
   
    path('account/profile/edit/', views.edit_profile, name = 'edit_profile'),
    path('change-password/', views.change_password, name = 'change_password'),
    path('reset-password/', PasswordResetView.as_view(template_name='blog/reset_password.html', 
    success_url=reverse_lazy('blog:password_reset_done'), 
    email_template_name = 'blog/reset_password_email.html'), name='reset_password'), 
   
    path('reset-password/done/', PasswordResetDoneView.as_view(template_name='blog/password_reset_done.html'), 
    name='password_reset_done'),
    
    path('reset-password/confirm/<uidb64>/<token>/',
    PasswordResetConfirmView.as_view(template_name='blog/password_reset_confirm.html', success_url=reverse_lazy('blog:password_reset_complete')), 
    name='password_reset_confirm'),
    
    path('reset-password/complete/', PasswordResetCompleteView.as_view(template_name='blog/password_reset_complete.html'), name='password_reset_complete'),

]
