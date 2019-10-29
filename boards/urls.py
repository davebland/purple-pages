""" URL config for board views """

from django.urls import path
from .views import display_single_board

urlpatterns = [
    path('<int:board_pk>/', display_single_board),
]