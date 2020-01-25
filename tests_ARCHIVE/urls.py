""" Test URL Patterns for Development Use """

from django.urls import path
from django.views.defaults import page_not_found

# Test error views
def test_404_view(request):
    return page_not_found(request, None)

urlpatterns = [
    path('404/', test_404_view),
]