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

from home.views import home, notice_boards
from boards import urls as urls_boards
from tests import urls as urls_test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('boards', notice_boards, name="boards"),
    path('boards/', include(urls_boards)),
    path('test/', include(urls_test))
]
