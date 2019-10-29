from django.db import models

from boards.models import Board

class Advert(models.Model):
    """ Data model for adverts """
    title = models.CharField(max_length=30)
    textContent = models.TextField(default="")
    on_boards = models.ManyToManyField(Board)

    def __str__(self):
        return self.title
