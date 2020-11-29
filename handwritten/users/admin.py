
# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Models
from handwritten.users.models import User

class CustomUserAdmin(UserAdmin):
    """ Model Admin """
    list_display = ('email','username','first_name', 'last_name')

admin.site.register(User,CustomUserAdmin)