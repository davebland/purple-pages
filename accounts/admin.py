from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import PPUser, Payment

# Register custom user and other models
admin.site.register(PPUser, UserAdmin)
admin.site.register(Payment)