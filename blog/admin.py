from django.contrib import admin
from blog.models import UserProfile
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.site_header="Admin"

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'phone', 'user_info')

    def user_info(self, obj):
        return obj.description
    
    def get_queryset(self, request):
        #inhearet normal queryset
        qs = super(UserProfileAdmin, self).get_queryset(request)
        #customize quersyset responses
        qs = qs.order_by('city')
        return qs

    user_info.short_description = 'Info'

#Rename what is desplayed from user_info to INFO
admin.site.register(UserProfile, UserProfileAdmin)
