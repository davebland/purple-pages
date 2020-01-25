from django.contrib import admin

from .models import Payment, Subscription

admin.site.register(Payment)
admin.site.register(Subscription)