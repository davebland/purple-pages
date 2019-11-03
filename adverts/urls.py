""" URL config for advert views """

from django.urls import path

from .views import advert_add_edit

urlpatterns = [
    path('new/', advert_add_edit, name='new_advert'),
    path('<int:advert_id>/edit', advert_add_edit, name='edit_advert'),
]