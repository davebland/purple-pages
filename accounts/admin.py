from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import PPUser

# Inline admin descriptor
class PPUserInline(admin.StackedInline):
    model = PPUser
    can_delete = False
    verbose_name_plural = 'PPUser'

# New User admin
class UserAdmin(BaseUserAdmin):
    inlines = (PPUserInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)