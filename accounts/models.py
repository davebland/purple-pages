from django.db import models
from django.contrib.auth.models import User

from boards.models import Board

class PPUser(models.Model):
    """ Data model for a Purple Pages User (extends django User) """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favourite_board = models.ForeignKey(Board, on_delete=models.SET_NULL, null=True, blank=True)