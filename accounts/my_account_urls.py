""" URL config for my_account views """

from django.urls import path

from .views import my_account

urlpatterns = [    
    path('', my_account, name="my_account"),
]