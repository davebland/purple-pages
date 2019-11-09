from django.db import models
from django.contrib.auth.models import User

from boards.models import Board

class PPUser(User):
    """ Data model for a Purple Pages User (extends django User) """
    favourite_board = models.ForeignKey(Board, on_delete=models.SET_NULL, null=True, blank=True)