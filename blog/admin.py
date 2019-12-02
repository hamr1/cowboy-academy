from django.contrib import admin
from blog.models import MentorProfile, MenteeProfile, User
from django.contrib.auth.admin import UserAdmin
# import pandas as pd 
# import numpy as np 


# Register your models here.
admin.site.site_header="Admin"

admin.site.register(User)

admin.site.register(MenteeProfile)

admin.site.register(MentorProfile)

# class MentorProfileAdmin(admin.ModelAdmin):
#     #define your list display or fieldsets
#      ....
#      ....

#      #now need to define urls for custom button in admin template file
#      def get_urls(self):
#         """
#         generate urls for methods. and attach with admin url
#         :param self:
#         """
#         urls = super().get_urls()
#         my_urls = [
#             path('match_mentee', self.match_mentee),
#         ]
#         return my_urls + urls


      
#         def match_mentee(self, request):
#             users = User.objects.filter(is_active=True)
            
#             MenteeProfile.object.filter(has_match=False)
            
#             MentorProfile.object.filter(at_capacity=False)



#             ids = [user.id for user in users if user.role == role]
#             return users.filter(id__in=ids)
        

#         self.message_user(request, "mentor has been assigned to mentee")
#         return HttpResponseRedirect("../")