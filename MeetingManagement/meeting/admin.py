

# Register your models here.
from django.contrib import admin

from meeting.models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class UserModel(UserAdmin):
    list_display = ['username', 'get_user_type_display']


# Register your models here.
admin.site.register(CustomUser, UserModel)