""" URL config for account views """

from django.urls import path, include
from .views import my_account

urlpatterns = [    
    path('', my_account, name="my_account"),
    path('', include('django.contrib.auth.urls')),
]