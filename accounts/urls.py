""" URL config for account views """

from django.urls import path, include

from .views import my_account, my_ads

urlpatterns = [
    path('', my_account, name="my_account"),
    path('my_ads/', my_ads, name="my_ads"),
    path('', include('django.contrib.auth.urls')),
]