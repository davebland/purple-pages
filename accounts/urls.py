""" URL config for account views """

from django.urls import path, include
from .views import my_account

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('my_account', my_account, name="my_account"),
]