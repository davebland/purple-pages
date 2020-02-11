""" URL config for account views """

from django.urls import path, include
from django.contrib.auth import urls as auth_urls
from django.contrib.auth import views as auth_views

from .forms import PPAuthenticationForm, PPPasswordResetForm
from .views import my_account, my_ads

urlpatterns = [
    path('', my_account, name="my_account"),
    #path('my_ads/', my_ads, name="my_ads"),
    path('login/', auth_views.LoginView.as_view(authentication_form=PPAuthenticationForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('password_change/', auth_views.PasswordChangeView.as_view(extra_context={'page_title':'Change Password'})),
    #path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(extra_context={'page_title':'Password Changed!'})),
    path('password_reset/', auth_views.PasswordResetView.as_view(form_class=PPPasswordResetForm), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #path('reset/done/', auth_views.PasswordResetCompleteView.as_view(extra_context={'page_title':'Password Reset!'})),
    #path('', include(auth_urls)),
]