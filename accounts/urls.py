""" URL config for account views """

from django.urls import path, include
from django.contrib.auth import urls as auth_urls
from django.contrib.auth import views as auth_views

from .forms import PPAuthenticationForm
from .views import my_account, my_ads

urlpatterns = [
    #path('', my_account, name="my_account"),
    #path('my_ads/', my_ads, name="my_ads"),
    path('login/', auth_views.LoginView.as_view(authentication_form=PPAuthenticationForm), name="login"),
    path('logout/', auth_views.LogoutView.as_view()),
    #path('password_change/', auth_views.PasswordChangeView.as_view(extra_context={'page_title':'Change Password'})),
    #path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(extra_context={'page_title':'Password Changed!'})),
    #path('password_reset/', auth_views.PasswordResetView.as_view(extra_context={'page_title':'Request Password Reset'})),
    #path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(extra_context={'page_title':'Password Reset Request Done'})),
    #path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(extra_context={'page_title':'Reset Your Password'})),
    #path('reset/done/', auth_views.PasswordResetCompleteView.as_view(extra_context={'page_title':'Password Reset!'})),
    #path('', include(auth_urls)),
]