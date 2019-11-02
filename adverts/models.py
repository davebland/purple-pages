from django.db import models
from django.contrib.auth.models import User

from boards.models import Board

class Advert(models.Model):
    """ Data model for adverts """
    title = models.CharField(max_length=30)
    textContent = models.TextField(default="")
    
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    on_boards = models.ManyToManyField(Board)

    def __str__(self):
        return self.title
