""" URL config for account views """

from django.urls import path, include
from django.contrib.auth import urls as auth_urls
from django.contrib.auth import views as auth_views

from .views import my_account, my_ads

urlpatterns = [
    path('', my_account, name="my_account"),
    path('my_ads/', my_ads, name="my_ads"),
    path('login/', auth_views.LoginView.as_view(extra_context={'page_title':'Please Login'})),
    path('', include(auth_urls)),
]