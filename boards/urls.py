""" URL config for board views """

from django.urls import path
from .views import notice_boards, display_single_board, set_favourite_board

urlpatterns = [
    path('', notice_boards, name="notice_boards"),
    path('<int:board_pk>/', display_single_board, name="display_single_board"),
    path('<int:board_pk>/set_as_favourite/', set_favourite_board, {'set_unset':True}, name="set_favourite_board"),
    path('<int:board_pk>/unset_as_favourite/', set_favourite_board, name="unset_favourite_board"),
    #path('create_board/', create_notice_board, name="create_notice_board"),
]