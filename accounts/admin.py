from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import PPUser

# Register custom user
admin.site.register(PPUser, UserAdmin)