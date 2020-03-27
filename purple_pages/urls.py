"""purple_pages URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from home.views import home, search 
from boards import urls as urls_boards
from adverts import urls as urls_adverts
#from tests import urls as urls_test
from accounts import urls as urls_accounts
#from subscriptions import urls as urls_subscriptions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('search/', search, name="search"),
    path('boards/', include(urls_boards), name="notice_boards"),
    path('adverts/', include(urls_adverts)),
    #path('test/', include(urls_test)),
    path('account/', include(urls_accounts)),
    #path('subscription/', include(urls_subscriptions),)
]