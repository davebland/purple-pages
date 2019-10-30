""" URL config for board views """

from django.urls import path
from .views import display_single_board, set_favourite_board

urlpatterns = [
    path('<int:board_pk>/', display_single_board, name="display_single_board"),
    path('set_favourite', set_favourite_board, name="set_favourite_board"),
]