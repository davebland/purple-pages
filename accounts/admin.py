from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import PPUser, Payment

# Create a custom user admin for PPUser
class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('favourite_board','subscription_expiry',)
    fieldsets = UserAdmin.fieldsets + (
        ("Purple Pages", {'fields': ('favourite_board', 'subscription_expiry')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Purple Pages", {'fields': ('favourite_board', 'subscription_expiry')}),
    )

# Register custom user and other models
admin.site.register(PPUser, CustomUserAdmin)
admin.site.register(Payment)