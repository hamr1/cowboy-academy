from django.contrib import admin
from blog.models import MentorProfile, MenteeProfile, User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.site_header="Admin"

admin.site.register(User)