""" URL config for subscription views """

from django.urls import path
from .views import subscription_overview

urlpatterns = [
    path('', subscription_overview, name="subscription_overview"),
]