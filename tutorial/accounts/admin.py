from django.contrib import admin
from .models import Userprofile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_info', 'city', 'website', 'phone')


    def user_info(self, obj):
        return obj.description
    def get_queryset(self, request):
        queryset = super(UserProfileAdmin,self).get_queryset(request)
        queryset = queryset.order_by('-phone','user')
        return queryset


    user_info.short_description = 'Info'


admin.site.register(Userprofile, UserProfileAdmin)
admin.site.site_header='Administration'


